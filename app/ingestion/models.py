from dataclasses import dataclass

@dataclass
class PageContent:
    text: str
    source: str
    page: int
    
@dataclass
class Chunk:
    text: str
    source: str
    page: int
    chunk_index: int    