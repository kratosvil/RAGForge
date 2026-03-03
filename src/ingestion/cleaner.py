import re

def clean_text(text: str) -> str:
    # Normaliza espacios múltiples
    text = re.sub(r"[ \t]+", " ", text)

    # Preserva saltos de párrafo reales (línea vacía entre bloques)
    text = re.sub(r"\n\s*\n", "\n\n", text)

    # Convierte saltos de línea simples a espacio (texto fluido de pypdf)
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

    return text.strip()
