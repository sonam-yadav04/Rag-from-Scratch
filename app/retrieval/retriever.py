from app.ingestion.models import Chunk
from app.retrieval.embedder import embed_query
from app.retrieval.vector_store import search

DEFAULT_K = 4
 # a starting guess: calibrate it on your own data (step 4)
DEFAULT_MIN_SCORE = 0.30 

def retrieve(
    question: str,
    k: int = DEFAULT_K,
    min_score: float = DEFAULT_MIN_SCORE,
    where: dict | None = None,
)->list[Chunk]:
    """Return up to k chunks scoring at least min_score, best first. May return []."""
    if k <= 0:
        raise ValueError("k must be positive")
    
    query_vector = embed_query(question)   # raises on an empty question
    hits = search(query_vector, k=k, where=where)

    return [
        Chunk(h["text"], h["source"], h["page"], h["chunk_index"], round(h["score"], 4))
        for h in hits
        if h["score"] >= min_score
    ]
