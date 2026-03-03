from fastapi import FastAPI
from ingestion.pipeline import run_ingestion
from embeddings.indexer import index_pdf

app = FastAPI(title="RAGForge API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "ragforge-api"}

@app.post("/index")
def index():
    count = index_pdf("/app/data/raw/kubernetes_basics.pdf")
    return {"indexed_chunks": count}

@app.get("/ingest-test")
def ingest_test():
    chunks = run_ingestion("/app/data/raw/kubernetes_basics.pdf")
    return {
        "total_chunks": len(chunks),
        "sample_chunk": chunks[0] if chunks else None
    }
