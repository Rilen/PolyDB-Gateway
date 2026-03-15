from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yaml
import os

app = FastAPI(title="PolyDB Gateway", version="0.1.0")

class QueryRequest(BaseModel):
    database: str
    query: str

@app.get("/")
async def root():
    return {"message": "PolyDB Gateway is running", "version": "0.1.0"}

@app.post("/query")
async def execute_query(request: QueryRequest):
    # TODO: Implement connection manager and query engine
    return {
        "database": request.database,
        "query": request.query,
        "status": "not_implemented",
        "message": "Query engine coming soon"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
