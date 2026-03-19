from fastapi import FastAPI
from src.chatbot import ask
from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str

app = FastAPI()

@app.post("/ask")

def ask_question(payload: QuestionRequest):

    answer = ask(payload.question)

    return {"answer": answer}
