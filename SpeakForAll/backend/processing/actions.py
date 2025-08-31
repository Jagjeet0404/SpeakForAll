def extract_actions(text: str):
    actions = []
    for line in text.splitlines():
        if any(word in line.lower() for word in ["must", "should", "need to", "action"]):
            actions.append(line.strip())
    return actions
