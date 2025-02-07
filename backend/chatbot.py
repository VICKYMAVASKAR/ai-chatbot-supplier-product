from langgraph import Graph
from langchain.chat_models import ChatOpenAI
from sqlalchemy.orm import Session
from database import SessionLocal, Product, Supplier

llm = ChatOpenAI(model_name="gpt-3.5-turbo")

def fetch_product_info(query):
    session = SessionLocal()
    products = session.query(Product).all()  # Fetch all products (modify for filtering)
    session.close()
    return products

def get_chatbot_response(query):
    context = fetch_product_info(query)
    response = llm.predict(f"Summarize the following products: {context}")
    return response

workflow = Graph()
workflow.add_node("chat", get_chatbot_response)
workflow.set_entry_point("chat")
