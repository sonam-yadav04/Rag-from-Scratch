from dataclasses import dataclass, field
from typing import Any, Dict
from sqlalchemy import BaseModel


@dataclass
class Document:
    """Represents an extracted page or document."""
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class TextChunk:
    """Represents a text chunk ready for embedding and indexing."""
    chunk_id: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)
