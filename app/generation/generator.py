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