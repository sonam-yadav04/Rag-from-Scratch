import io
import re
from pathlib import Path
from typing  import List,Union
from pypdf import PdfReader
# from app.ingestion.models import Document

def clean_text(text:str)->str:
    """cleans raw PDF text:fixes line breaks,removes null bytes and multiple spaces."""
