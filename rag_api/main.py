# main.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
from rag_chain_setup import get_rag_chain

app = FastAPI()
rag_chain, memory = get_rag_chain()

class ChatRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "Multilingual RAG API is running!"}

@app.post("/chat")
def chat(request: ChatRequest):
    user_input = request.query
    answer = rag_chain.invoke(user_input)

    # Save to memory for continuity
    memory.save_context({"question": user_input}, {"output": answer})

    return {"response": answer}
