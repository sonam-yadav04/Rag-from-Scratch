
import re
from rank_bm25 import BM25Okapi


def tokenize(text: str) -> list[str]:
    """
    Convert text into lowercase tokens.
    """
    if not text or not text.strip():
        return []

    return re.findall(r"\b\w+\b", text.lower())


