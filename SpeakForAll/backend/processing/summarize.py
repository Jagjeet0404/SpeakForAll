def summarize_text(text: str) -> str:
    sentences = text.split('.')[:3]
    return '.'.join(sentences).strip()
