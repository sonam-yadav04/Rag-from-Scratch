from app.retrieval.bm25 import BM25Retriever

documents = [
    {
        "text": "I developed backend APIs using Python and FastAPI.",
        "source": "resume.pdf",
        "page": 1
    },
    {
        "text": "I used React and TypeScript to build frontend applications.",
        "source": "resume.pdf",
        "page": 2
    },
    {
        "text": "Redis was used for caching in the backend application.",
        "source": "project.pdf",
        "page": 1
    },
   
]
retriever = BM25Retriever(documents)
query = "Python FastAPI backend"

res = retriever.search(query, k=3)
print("\nBM25 Search Results:")

for res in res:
    print("\nText:", res["text"])
    print("Score:", round(res["bm25_score"], 4))
    print("Source:", res["source"])