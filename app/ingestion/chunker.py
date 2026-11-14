from app.ingestion.models import Chunk


def chunk_text(text: str, size: int = 500, overlap: int = 100) -> list[str]:
    """Split text into overlapping pieces of at most `size` characters."""
    if size <= 0 or overlap < 0 or overlap >= size:
        raise ValueError("need 0 <= overlap < size")

    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        if end < len(text):
            cut = max(text.rfind("\n", start, end), text.rfind(" ", start, end))
            if cut > start + size // 2:
                end = cut

        piece = text[start:end].strip()
        if piece:
            chunks.append(piece)
        if end >= len(text):
            break

        start = max(end - overlap, start + 1)
        nxt = text.find(" ", start, end)
        if nxt != -1:
            start = nxt + 1
    return chunks


def chunk_pages(pages, size: int = 500, overlap: int = 100) -> list[Chunk]:
    """Chunk every page, copying source and page number onto each chunk."""
    chunks = []
    for page in pages:
        for piece in chunk_text(page.text, size, overlap):
            chunks.append(Chunk(piece, page.source, page.page, len(chunks)))
    return chunks