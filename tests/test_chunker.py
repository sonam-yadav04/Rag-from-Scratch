import pytest

from app.ingestion.chunker import chunk_pages, chunk_text
from app.ingestion.models import PageContent

WORDS = " ".join(f"w{i}" for i in range(300))


def test_short_text_is_one_chunk():
    assert chunk_text("hello world", size=500, overlap=50) == ["hello world"]


def test_empty_text_gives_no_chunks():
    assert chunk_text("   ") == []


def test_chunks_never_exceed_size():
    assert all(len(c) <= 100 for c in chunk_text(WORDS, size=100, overlap=20))


def test_no_words_are_lost():
    chunks = chunk_text(WORDS, size=100, overlap=20)
    seen = {w for c in chunks for w in c.split()}
    assert seen == set(WORDS.split())


def test_consecutive_chunks_overlap():
    chunks = chunk_text(WORDS, size=100, overlap=20)
    assert chunks[0].split()[-1] in chunks[1].split()


def test_text_without_spaces_terminates():
    chunks = chunk_text("a" * 1200, size=500, overlap=100)
    assert len(chunks) == 3
    assert all(len(c) <= 500 for c in chunks)


def test_bad_overlap_raises():
    with pytest.raises(ValueError):
        chunk_text("anything", size=100, overlap=100)


def test_chunk_pages_keeps_metadata_and_numbers_chunks():
    pages = [PageContent(WORDS, "a.pdf", 1), PageContent("short text", "a.pdf", 2)]
    chunks = chunk_pages(pages, size=100, overlap=20)
    assert [c.chunk_index for c in chunks] == list(range(len(chunks)))
    assert chunks[-1].page == 2 and chunks[-1].source == "a.pdf"