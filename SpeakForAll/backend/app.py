from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from processing import summarize, simplify, actions, keywords, tts

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "API is running"}

# Process text
@app.post("/process_text")
async def process_text(text: str = Form(...)):
    return {
        "summary": summarize.summarize_text(text),
        "simplified": simplify.simplify_text(text),
        "actions": actions.extract_actions(text),
        "keywords": keywords.extract_keywords(text)
    }

# Text-to-speech
@app.post("/tts")
async def generate_tts(text: str = Form(...)):
    path = tts.text_to_speech(text)
    return {"audio_path": path}
