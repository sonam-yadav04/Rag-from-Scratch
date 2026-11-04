from GroqClient import GroqClient
from fastapi import HTTPException, FastAPI
from dotenv import load_dotenv
load_dotenv()
import os

client = GroqClient(api_key=os.getenv("GROQ_APP_KEY"))

def build_prompt(question, context):
    prompt = f"""
    Answer the question using only the
    provided context.

    Context:
    {context}

    Question:
    {question}

    If the answer is not available in the
    context, say you don't know.
    """
    return prompt

