from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import yaml
import os
from typing import List, Dict, Any

app = FastAPI(
    title="PolyDB Gateway",
    description="Unified API for multi-database observable access",
    version="0.1.0"
)

def get_db_config():
    config_path = "config/databases.yaml"
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    return {}

class QueryRequest(BaseModel):
    database: str
    query: str

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "PolyDB Gateway",
        "author": "Rilen T. L.",
        "docs": "/docs"
    }

@app.post("/query")
async def execute_query(request: QueryRequest):
    configs = get_db_config()
    db_name = request.database
    
    if db_name not in configs.get('databases', {}):
        raise HTTPException(status_code=404, detail=f"Database '{db_name}' not configured")
    
    db_config = configs['databases'][db_name]
    
    if db_config['type'] == 'sqlite':
        try:
            conn = sqlite3.connect(db_config['path'])
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(request.query)
            
            if request.query.strip().upper().startswith("SELECT"):
                rows = cursor.fetchall()
                results = [dict(row) for row in rows]
                return {
                    "database": db_name,
                    "rows_count": len(results),
                    "data": results,
                    "status": "success"
                }
            else:
                conn.commit()
                return {
                    "database": db_name,
                    "status": "success",
                    "affected_rows": cursor.rowcount
                }
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        finally:
            conn.close()
    
    return {
        "database": db_name,
        "status": "pending",
        "message": f"Adapter for {db_config['type']} is being implemented in the next phase."
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
