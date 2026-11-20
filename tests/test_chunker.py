import pytest
from app.ingestion.chunker import chunk_text


def test_chunk_text():
    text = "sharing a text to chunk it properly"

    result = chunk_text(text, size=15, overlap=3)

    assert len(result) > 1
    assert all(isinstance(chunk, str) for chunk in result)


def test_text_smaller_than_chunk_size():
    text = "Hello world"

    result = chunk_text(text, size=100, overlap=10)

    assert result == ["Hello world"]


def test_empty_text():
    result = chunk_text("")

    assert result == []

def test_no_empty_chunks():
    text = "Hello world this is a test"

    result = chunk_text(text, size=10, overlap=2)

    assert all(chunk.strip() for chunk in result)    