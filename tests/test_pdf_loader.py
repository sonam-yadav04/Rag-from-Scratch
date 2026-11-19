
import pytest
import pymupdf

from app.ingestion.pdf_loader import load_pdf


def create_pdf(path, text=None):
    """Create a temporary PDF for testing."""

    doc = pymupdf.open()
    page = doc.new_page()

    if text:
        page.insert_text((50, 50), text)

    doc.save(path)
    doc.close()


def test_load_valid_pdf(tmp_path):

    pdf_path = tmp_path / "sample.pdf"

    create_pdf(pdf_path, "This is a RAG test document.")

    pages = load_pdf(str(pdf_path))

    assert len(pages) == 1
    assert pages[0].page == 1
    assert pages[0].source == "sample.pdf"
    assert "RAG test document" in pages[0].text


def test_missing_pdf():

    with pytest.raises(FileNotFoundError):
        load_pdf("missing.pdf")


def test_invalid_extension(tmp_path):

    file_path = tmp_path / "sample.txt"
    file_path.write_text("Not a PDF")

    with pytest.raises(ValueError, match="Only .pdf"):
        load_pdf(str(file_path))


def test_empty_pdf(tmp_path):

    pdf_path = tmp_path / "empty.pdf"

    create_pdf(pdf_path)

    with pytest.raises(ValueError, match="No extractable text"):
        load_pdf(str(pdf_path))


def test_skip_blank_pages(tmp_path):

    pdf_path = tmp_path / "multiple_pages.pdf"

    doc = pymupdf.open()

    # Page 1 contains text
    page1 = doc.new_page()
    page1.insert_text((50, 50), "First page content")

    # Page 2 is blank
    doc.new_page()

    doc.save(pdf_path)
    doc.close()

    pages = load_pdf(str(pdf_path))

    assert len(pages) == 1
    assert pages[0].page == 1
