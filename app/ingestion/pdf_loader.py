import pymupdf
from pathlib import Path


def load_pdf(path: str) -> list[dict]:
    """Return one dict per page: {page_number, text, char_count}."""
    file = Path(path)
    if not file.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    pages = []
    with pymupdf.open(file) as doc:
        print(f"File: {file.name}")
        print(f"Total pages: {doc.page_count}\n")

        for index, page in enumerate(doc):
            text = page.get_text().strip()
            pages.append({
                "page_number": index + 1,
                "text": text,
                "char_count": len(text),
            })
            print(f"Page {index + 1}: {len(text)} characters")

    return pages


if __name__ == "__main__":
    load_pdf("full-stack_resume(1).pdf")