from fastapi import FastAPI

klu = FastAPI(
    title="AI Tutor",
    description="AI Tutor PBL Project",
    version="1.0.0",
)


@klu.get("/")
def home():
    return {"message": "Welcome to AI Tutor Project"}


@klu.get("/university")
def university():
    return {"message": "KLUniversity"}


@klu.get("/ask")
def ask():
    return {"message": "What is LLM?", "answer": "LARGE LANGUAGE MODEL"}
