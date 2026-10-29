import io
import re
from pathlib import Path
from typing  import List,Union
from pypdf import PdfReader
from app.ingestion.models import Document

def clean_text(text:str)->str:
    """cleans raw PDF text:fixes line breaks,removes null bytes and multiple spaces."""
    if not text:
        return ""
    # remove null bytes
    text = text.replace("\x00", "")
    #normalize win/mac line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n") 
    # Fix hyphenated line breaks (e.g., 'trans-\nformer' -> 'transformer')
    text = re.sub(r"(\w+)-\n(\w+)",r"\1\2", text)
    # Replace 3 or more newlines with double newline
    text = re.sub(r"\n{3,}","\n\n", text)
    # Normalize multiple whitespace characters except newlines
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()




    
