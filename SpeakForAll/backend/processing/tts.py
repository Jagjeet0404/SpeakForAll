import pyttsx3, os, uuid

def text_to_speech(text: str) -> str:
    engine = pyttsx3.init()
    filename = f"/tmp/{uuid.uuid4().hex}.mp3"
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename
