from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
_model = None

def get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model

def embed_texts(texts: list[str]) -> list[list[float]]:
    # return type will be - [[0.9293 , 0.2932]]- list inside list , containing float value.
    """Embed many texts at once. Returns one unit-length vector per text."""
    if not texts:
        return []
    vectors = get_model().encode(texts, normalize_embeddings=True, batch_size=32)
    #normally model returns numpy array we convert it to python list
    return vectors.tolist()

def embed_query(question: str) -> list[float]:
    """Embed a single question with the same model used for documents."""
    question = question.strip()
    if not question:
        raise ValueError("Question is empty")
    return embed_texts([question])[0]

if __name__ == "__main__":
    a = embed_query("I have 2 years of backend experience")
    b = embed_query("Worked on FastAPI services for two years")
    c = embed_query("The weather in Bengaluru is rainy")
    #A dot product is a mathematical operation that takes two vectors and returns one single number (a scalar).
    dot = lambda x, y: sum(p * q for p, q in zip(x, y))
    #zip() pairs corresponding elements from both vectors.
    print("dimension:", len(a))
    print("input limit (tokens):", get_model().max_seq_length)
    print("backend vs fastapi:", round(dot(a, b), 3))
    print("backend vs weather:", round(dot(a, c), 3))