import re

def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100):
    # Divide en oraciones para no cortar en medio de una frase
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:
            current_chunk += (" " if current_chunk else "") + sentence
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            # Inicia nuevo chunk con overlap del anterior
            current_chunk = current_chunk[-overlap:] + " " + sentence if overlap and current_chunk else sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
