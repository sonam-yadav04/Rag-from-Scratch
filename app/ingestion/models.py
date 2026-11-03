# from dataclasses import dataclass, field
# from typing import Any, Dict
# from sqlalchemy import BaseModel


# @dataclass
# class Document:
#     """Represents an extracted page or document."""
#     content: str
#     metadata: Dict[str, Any] = field(default_factory=dict)

# @dataclass
# class TextChunk:
#     """Represents a text chunk ready for embedding and indexing."""
#     chunk_id: str
#     content: str
#     metadata: Dict[str, Any] = field(default_factory=dict)


from pydantic import BaseModel, Field
from typing import Literal


class ExtractedPage(BaseModel):
    page_number: int = Field(ge=1)
    text: str
    character_count: int = Field(ge=0)
    image_count: int = Field(ge=0)
    extraction_status: Literal[
        "text_extracted",
        "possible_scanned_page",
        "empty_page"
    ]


class ExtractedDocument(BaseModel):
    document_id: str
    filename: str
    total_pages: int = Field(ge=0)
    pages: list[ExtractedPage]

