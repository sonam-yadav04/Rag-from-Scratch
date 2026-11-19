from fastapi import FastAPI
# from app.data import documents

app = FastAPI(title="RAG From Scratch")

# app.include_router(
#     documents,
#     prefix="/documents",
#     tags=["Documents"]
# )


@app.get("/health", tags=["Health"])
def health_check():
    return {"message": "RAG API is running"}
