from fastapi import FastAPI

from app.api.routes.documents import router as documents_router

app = FastAPI(title="RAG From Scratch")

app.include_router(
    documents_router,
    prefix="/documents",
    tags=["Documents"]
)


@app.get("/")
def home():
    return {"message": "RAG API is running"}