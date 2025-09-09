from fastapi import FastAPI
from pydantic import BaseModel
from models.translator import translate, SupportedLang
from models.recommender import TFIDFRecommender
from models.resume_parser import extract_keywords

app = FastAPI(title="Multilingual Job Assistant — 20% Prototype")

recs = TFIDFRecommender()

class TranslateReq(BaseModel):
    text: str
    src: SupportedLang = "en"
    tgt: SupportedLang = "en"

class RecommendReq(BaseModel):
    query: str
    top_k: int = 5

class ChatReq(BaseModel):
    message: str
    lang: SupportedLang = "en"

@app.get("/")
def root():
    return {"ok": True, "service": "multilingual-job-assistant-20pct"}

@app.post("/translate")
def do_translate(req: TranslateReq):
    return {"translated": translate(req.text, req.src, req.tgt)}

@app.post("/recommend")
def recommend(req: RecommendReq):
    results = recs.recommend(req.query, req.top_k)
    return {"results": results}

@app.post("/chat")
def chat(req: ChatReq):
    msg = req.message.lower().strip()
    if "hello" in msg or "hi" in msg:
        reply = "Hello! I can recommend jobs and translate queries. Try: 'recommend backend python in Bengaluru'."
    elif "recommend" in msg or "job" in msg:
        reply = "Sure! Tell me your skills or desired role & city (e.g., 'python backend Bengaluru')."
    elif "help" in msg:
        reply = "Endpoints: /translate, /recommend, /chat. Use the sample frontend to try them quickly."
    else:
        reply = "I'm a basic demo bot. Ask me for job recommendations or translations."
    return {"reply": reply}

# Utility endpoint for resume keyword extraction (demo)
class ResumeReq(BaseModel):
    text: str

@app.post("/parse_resume")
def parse_resume(req: ResumeReq):
    keywords = extract_keywords(req.text)
    return {"keywords": keywords}