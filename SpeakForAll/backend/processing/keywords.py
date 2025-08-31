def extract_keywords(text: str):
    words = text.split()
    return list(set([w.strip('.,') for w in words if len(w) > 6]))[:5]
