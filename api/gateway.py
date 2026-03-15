from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import sqlite3
import yaml
import os
import time
from typing import List, Dict, Any
from prometheus_client import Counter, Histogram, make_asgi_app

# --- Métricas do Prometheus ---
QUERY_COUNT = Counter(
    "polydb_gateway_queries_total", 
    "Total de queries executadas", 
    ["database", "status"]
)
QUERY_LATENCY = Histogram(
    "polydb_gateway_query_latency_seconds", 
    "Latência das queries em segundos", 
    ["database"]
)

app = FastAPI(
    title="PolyDB Gateway",
    description="Unified API for multi-database observable access",
    version="0.1.0"
)

# Adiciona o endpoint de métricas para o Prometheus
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

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
        "docs": "/docs",
        "metrics": "/metrics"
    }

@app.post("/query")
async def execute_query(request: QueryRequest):
    configs = get_db_config()
    db_name = request.database
    
    if db_name not in configs.get('databases', {}):
        QUERY_COUNT.labels(database=db_name, status="error").inc()
        raise HTTPException(status_code=404, detail=f"Database '{db_name}' not configured")
    
    db_config = configs['databases'][db_name]
    start_time = time.time()
    
    try:
        # --- Lógica para SQLite ---
        if db_config['type'] == 'sqlite':
            conn = sqlite3.connect(db_config['path'])
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(request.query)
            
            if request.query.strip().upper().startswith("SELECT"):
                rows = cursor.fetchall()
                results = [dict(row) for row in rows]
                output = {
                    "database": db_name,
                    "rows_count": len(results),
                    "data": results,
                    "status": "success"
                }
            else:
                conn.commit()
                output = {
                    "database": db_name,
                    "status": "success",
                    "affected_rows": cursor.rowcount
                }
            conn.close()
            
            QUERY_COUNT.labels(database=db_name, status="success").inc()
            QUERY_LATENCY.labels(database=db_name).observe(time.time() - start_time)
            return output

        # --- Lógica para PostgreSQL ---
        elif db_config['type'] == 'postgres':
            import psycopg2
            from psycopg2.extras import RealDictCursor
            
            conn = psycopg2.connect(
                host=db_config['host'],
                port=db_config['port'],
                database=db_config['database'],
                user=db_config['user'],
                password=db_config['password']
            )
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(request.query)
            
            if request.query.strip().upper().startswith("SELECT"):
                results = cursor.fetchall()
                output = {
                    "database": db_name,
                    "rows_count": len(results),
                    "data": results,
                    "status": "success"
                }
            else:
                conn.commit()
                output = {
                    "database": db_name,
                    "status": "success",
                    "affected_rows": cursor.rowcount
                }
            cursor.close()
            conn.close()
            
            QUERY_COUNT.labels(database=db_name, status="success").inc()
            QUERY_LATENCY.labels(database=db_name).observe(time.time() - start_time)
            return output

        # --- Lógica para MySQL ---
        elif db_config['type'] == 'mysql':
            import pymysql
            
            conn = pymysql.connect(
                host=db_config['host'],
                port=int(db_config['port']),
                user=db_config['user'],
                password=db_config['password'],
                database=db_config['database'],
                cursorclass=pymysql.cursors.DictCursor
            )
            
            with conn.cursor() as cursor:
                cursor.execute(request.query)
                if request.query.strip().upper().startswith("SELECT"):
                    results = cursor.fetchall()
                    output = {
                        "database": db_name,
                        "rows_count": len(results),
                        "data": results,
                        "status": "success"
                    }
                else:
                    conn.commit()
                    output = {
                        "database": db_name,
                        "status": "success",
                        "affected_rows": cursor.rowcount
                    }
            conn.close()
            
            QUERY_COUNT.labels(database=db_name, status="success").inc()
            QUERY_LATENCY.labels(database=db_name).observe(time.time() - start_time)
            return output

        else:
            QUERY_COUNT.labels(database=db_name, status="unsupported").inc()
            return {
                "database": db_name,
                "status": "error",
                "message": f"Tipo de banco {db_config['type']} não suportado."
            }

    except Exception as e:
        QUERY_COUNT.labels(database=db_name, status="error").inc()
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": time.time()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
