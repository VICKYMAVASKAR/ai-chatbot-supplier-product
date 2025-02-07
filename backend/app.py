from fastapi import FastAPI, Query
from chatbot import get_chatbot_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to AI Chatbot for Supplier & Product Info!"}

@app.get("/chat")
def chat(query: str = Query(..., description="User query")):
    response = get_chatbot_response(query)
    return {"response": response}
