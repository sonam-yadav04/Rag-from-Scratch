
from app.pdf_loader import extract_text_from_pdf

file_path = "data/raw/sample.pdf"

pages = extract_text_from_pdf(file_path)

for page in pages:
    print(f"\n--- Page {page['page_number']} ---")
    print(page["text"])
