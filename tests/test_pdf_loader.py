import pymupdf
import unittest

from app.ingestion.pdf_loader import load_pdf

def make_pdf(path, page_texts):
    """Create a PDF; each item in page_texts becomes one page ('' = blank page)."""
    doc = pymupdf.open()
    for text in page_texts:
        page = doc.new_page()
        if text:
            page.insert_text((72, 72), text)
    doc.save(path)
    doc.close()
    return path



if __name__ == "__main__":
    unittest.main()