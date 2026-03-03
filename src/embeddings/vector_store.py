import chromadb
import os

def get_client():
    return chromadb.HttpClient(
        host=os.getenv("CHROMA_HOST", "chroma"),
        port=int(os.getenv("CHROMA_PORT", 8000))
    )

def get_or_create_collection():
    client = get_client()
    return client.get_or_create_collection(
        name="k8s_basics"
    )
