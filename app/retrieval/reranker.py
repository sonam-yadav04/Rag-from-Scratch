from sentence_transformers import CrossEncoder

MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

_model = None

def get_reranker():
    global _model
    if _model is None:
      _model = CrossEncoder(MODEL_NAME)
    return _model

def rerank(
      question:str,
      chunks:list,
      top_n:int=3,
      )->list[dict]:
    if not question.strip(): 
        raise ValueError("question can not be empty")
    if top_n <=0:
        raise ValueError("TOP_N must be positive")
    
    if not chunks:
        return []
    model = get_reranker()
    pairs = [
        (question,chunk.text)
        for chunk in chunks
    ]   
    scores = model.predict(pairs)
    ranked_chunks = []
    for chunk , score in zip(chunks,scores):
        ranked_chunks.append({
            "chunk":chunk,
            "rerank_score":float(score)
        })   
    ranked_chunks.sort(
        key=lambda item: item["rerank_score"],
        reverse=True
    ) 
    return ranked_chunks[:top_n]    