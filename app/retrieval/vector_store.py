import chromadb
from app.retrieval.embedder import embed_texts
#table name = collection  name 
COLLECTION_NAME = "rag_documents"
 # db client 
_client = None
#table 
_collection = None
from app.ingestion.models import Chunk


def get_collection():
    global _client, _collection
 
    if _collection is None:
        # creating persistent Client -If your application stops and restarts, your stored vectors remain available.
        _client = chromadb.PersistentClient(
            path="./chroma_db"
        )
        # create new collection if not exsits otherwise returns the exist collection
        _collection = _client.get_or_create_collection(
            name=COLLECTION_NAME,
            #hnsw:space configures cosine distance for vector comparison.
            metadata={"hnsw:space": "cosine"}
        )

    return _collection

def add_chunks(chunks:list[Chunk], embeddings :list[list[float]])->None:
    if not chunks:
        return
    if len(chunks) != len(embeddings):
        raise ValueError("numberof chunks and embedding must be equal")
    
    collection = get_collection()
    ids = []
    documents = []
    metadatas = []
    
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

