import chromadb
import os
#table name = collection  name 
COLLECTION_NAME = "rag_documents"
CHROMA_PATH = os.getenv("CHROMA_PATH", "./chroma_db")
 # db client 
_client = None
#table 
_collection = None
from app.ingestion.models import Chunk


def get_collection():
    global _client, _collection
 
    if _collection is None:
        # creating persistent Client -If your application stops and restarts, your stored vectors remain available.
        _client = chromadb.PersistentClient( path=CHROMA_PATH)
        # create new collection if not exsits otherwise returns the exist collection
        _collection = _client.get_or_create_collection(
            name=COLLECTION_NAME,
            #hnsw:space configures cosine distance for vector comparison.
            metadata={"hnsw:space": "cosine"}
        )

    return _collection
# for storying embeddings of the chunks 
def add_chunks(chunks:list[Chunk], embeddings:list[list[float]])->None:
    if not chunks:
        return
    if len(chunks) != len(embeddings):
        raise ValueError("number of chunks and embedding must be equal")
    
    collection = get_collection()
    ids = []
    documents = []
    metadatas = []
    
    for source in {c.source for c in chunks}:   # drop stale chunks from older versions
      collection.delete(where={"source": source})
    
    for chunk in chunks:
        chunk_id = (
            f"{chunk.source}_page{chunk.page}"
            f"_chunk{chunk.chunk_index}"
        ) 
        ids.append(chunk_id)
        documents.append(chunk.text)
        metadatas.append(
            {
                "source":chunk.source,
                "page": chunk.page,
                "chunk_index":chunk.chunk_index
            }
        )  
    
# add() inserts new records and raises an error if an ID already exists
# upsert() inserts new records or updates existing records with matching IDs.
     
    collection.upsert(
        ids= ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas
    ) 

def search(query_embedding: list[float], k: int = 4, where: dict | None = None) -> list[dict]:
    """Return up to k nearest chunks as dicts, nearest first, with score = 1 - distance."""
    collection = get_collection()
    total = collection.count()
    if total == 0:
        return []
    
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(k, total),
        where=where,
        include=["documents", "metadatas", "distances"],
    )
    hits = []
    for chunk_id ,text, meta, dist in zip(
        result["ids"][0],result["documents"][0],result["metadatas"][0], result["distances"][0]
    ):
        hits.append({
            "id": chunk_id,
            "text": text,
            "source": meta["source"],
            "page": meta["page"],
            "chunk_index": meta["chunk_index"],
            "score": 1 - dist,
        })
    return hits      
    

