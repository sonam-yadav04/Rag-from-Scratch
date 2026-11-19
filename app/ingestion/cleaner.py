import re
from app.ingestion.pdf_loader import load_pdf
def clean_text(text: str) -> str:
    """
    Clean extracted PDF text before passing it to the chunker.
    """
    if not text or not text.strip():
        return ""
    # 1. Normalize Windows and Mac line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # 2. Remove null characters
    text = text.replace("\x00", "")
    # 3. Remove unnecessary spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # 4. Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 5. Remove leading and trailing whitespace
    text = text.strip()

    return text

def clean_pdf(path: str):
    pages = load_pdf(path)
    cleaned_pages = []

    for page in pages:
        page.text = clean_text(page.text)

        if page.text:
            cleaned_pages.append(page)

    return cleaned_pages

if __name__ == "__main__":
    result = clean_pdf("data/documents/resume.pdf")
    print(f"Successfully cleaned {len(result)} pages")

    for page in result:
        print(f"\nPage: {page.page}")
        print(page.text[:1000])

# def clean_pages(pages: list[PageContent]) -> list[PageContent]:
#     """Clean every page, keeping source and page number intact."""
#     cleaned = []
#     for page in pages:
#         text = clean_text(page.text)
#         if text:
#             cleaned.append(replace(page, text=text))
#     if not cleaned:
#         raise ValueError("No text left after cleaning")
#     return cleaned

