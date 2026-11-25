from sentence_transformers import CrossEncoder

MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

_model = None

def get_reRanker():
     global  _model
     if _model is None:
        _model = CrossEncoder(MODEL_NAME)
         
     