from ingestion.loader import load_pdf
from ingestion.cleaner import clean_text
from ingestion.chunker import chunk_text

def run_ingestion(path: str):
    raw = load_pdf(path)
    clean = clean_text(raw)
    chunks = chunk_text(clean, chunk_size=500, overlap=50)

    return chunks
