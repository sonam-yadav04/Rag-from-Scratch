import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])
MODEL = "qwen/qwen3.8-27b"   # use whichever model name worked in your job tracker

client = GroqClient(api_key=os.getenv("GROQ_APP_KEY"))

def ask(messages):
    resp = client.chat.completions.create(
        model=MODEL, messages=messages, max_tokens=200
    )
    return resp.choices[0].message.content

    context = (
        "Employees receive 18 days of annual leave per year. "
        "Medical leave over 2 days requires a doctor's note."
    )

    prompt = f"""Answer using ONLY the context below.
    If the answer is not in the context, say "I don't know."

    Context:
    {context}

    Question: {question}"""

    print("\nWITH context:")
    print(ask([{"role": "user", "content": prompt}]))

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
    # client = Chat.completion.create(
    #     model="gpt-4o",
    #     messages =messages,
    #     temprature=0.7,
        
        
    # )

    # res = client.choices[0].message.content