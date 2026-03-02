import re

def clean_text(text: str) -> str:
    # remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # remove weird line breaks
    text = text.replace("\n", " ")

    return text.strip()
