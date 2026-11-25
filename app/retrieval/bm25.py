import re
from rank_bm25 import BM25Okapi

def tokenize(text:str)->list[str]:
    """converts text into lower case tokens"""
    if not text or not text.strip():
        return []
    #convert text into lowercase words so that Python and python are treated as the same token.
    return re.findall(r"\b\w+\b",text.lower())
 
class BM25Retriever:
    def __init__(self,documents:list[dict]):
        if not documents:
            raise ValueError("Docs can not be empty!")
        self.documents = documents
        
        #tokenize every document
        self.tokenized_corpus =[
            tokenize(doc["text"])
            for doc in documents
        ]
        # Initialize BM25
        self.bm25 = BM25Okapi(self.tokenized_corpus)
    def search(self, query:str,k:int=4)->list[dict]:
        if not query.strip():
            raise ValueError("query can not be empty")
        if k <= 0:
            raise ValueError("Value of k should be positive")
        
        query_tokens = tokenize(query)
        
        #calculate BM25 score
        scores = self.bm25.get_scores(query_tokens)
        
        #sort document by hightes score (desc)
        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i :scores[i],
            reverse=True
        )
        result = []
        for idx in ranked_indices[:k]:
            if scores[idx]<=0:
                continue
            result.append({
                **self.documents[idx],
                "bm25_score":float(scores[idx])
                
            })
        return result    
            
            
 


