import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "llama-3.1-8b-instant"

_client = None

def get_groq_client() -> Groq:
    global _client

    if _client is None:
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY is missing")

        _client = Groq(api_key=api_key)

    return _client

def generate_answer(context:str, question:str)->str:
    if not context.strip():
         return "I don't have enough information to answer this question."
    if not question.strip():  
        raise ValueError("question can not be empty")
    
    client = get_groq_client() 
    
    system_prompt = """
    You are a helpful AI assistant that answers questions
    using the provided context.

    Follow these rules:
    1. Answer only using the provided context.
    2. Do not make up or assume information.
    3. If the context does not contain the answer,
       clearly say that you don't have enough information.
    4. Give clear and concise answers.
    """
    user_prompt = f""""
    Context:
    {context}
    Question:
    {question}
    Answer 
    """
    
    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[ {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt} ],
        
        temperature=0.2 
    )
    
    return res.choices[0].message.content.strip()

if __name__ == "__main__":

    context = """
    Sonam has experience in Python and FastAPI.
    She has worked with MySQL, Redis and React.
    She completed a five-month internship.
    """

    question = "Which backend technologies does Sonam know?"
    answer = generate_answer(context, question)
    print("\nGenerated Answer:")
    print(answer)