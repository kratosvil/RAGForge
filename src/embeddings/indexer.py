from ingestion.pipeline import run_ingestion
from embeddings.client import generate_embedding
from embeddings.vector_store import get_or_create_collection

def index_pdf(path: str):
    chunks = run_ingestion(path)
    collection = get_or_create_collection()

    ids = []
    documents = []
    embeddings = []

    for i, chunk in enumerate(chunks):
        ids.append(f"chunk_{i}")
        documents.append(chunk)
        embeddings.append(generate_embedding(chunk))

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

    return len(chunks)
