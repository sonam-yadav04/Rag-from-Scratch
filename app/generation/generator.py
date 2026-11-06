from GroqClient import GroqClient
from fastapi import HTTPException, FastAPI
from dotenv import load_dotenv
load_dotenv()
import os
from groqClient import GroqClient

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

messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": build_prompt("What is the capital of France?", "France is a country in Europe.")
        }
 ]
client = Chat.completion.create(
    model="gpt-4o",
    messages =messages,
    temprature=0.7,
    
     
)

res = client.choices[0].message.content