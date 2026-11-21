from app.ingestion.models import Chunk

def chunk_text(text: str, size: int = 500, overlap: int = 100) -> list[str]:
    """Split text into overlapping pieces of at most `size` characters."""
    if size <= 0 or overlap < 0 or overlap >= size:
        raise ValueError("page size or overlap is incorrect")

    chunks = []
    s = 0
    while s < len(text):
        end = min(s + size, len(text))
        if end < len(text):
            cut = max(text.rfind("\n", s, end), text.rfind(" ", s, end))
            if cut > s + size // 2:
                end = cut

        piece = text[s:end].strip()
        if piece:
            chunks.append(piece)
        if end >= len(text):
            break

        s = max(end - overlap, s + 1)
        nxt = text.find(" ", s, end)
        if nxt != -1:
            s = nxt + 1
    return chunks


def chunk_pages(pages, size: int = 500, overlap: int = 100) -> list[Chunk]:
    """Chunk every page, copying source and page number onto each chunk."""
    chunks = []
    for page in pages:
        for piece in chunk_text(page.text, size, overlap):
            chunks.append(Chunk(piece, page.source, page.page, len(chunks)))
    return chunks