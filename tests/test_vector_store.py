from app.ingestion.models import Chunk
from app.retrieval.embedder import embed_texts
from app.retrieval.vector_store import add_chunks, get_collection
# import pytest
chunks = [
    Chunk("Python developer with FastAPI experience.", "test.pdf", 1, 0),
    Chunk("Experienced in MySQL and Redis.", "test.pdf", 1, 1)
]

texts = [chunk.text for chunk in chunks]

vectors = embed_texts(texts)

add_chunks(chunks, vectors)

collection = get_collection()

print("Stored records:", collection.count())