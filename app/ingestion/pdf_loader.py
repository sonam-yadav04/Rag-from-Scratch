from pathlib import Path
import pymupdf
#1 validate the file path and extension

def load_pdf(path):
    file = Path(path)
    if not file.exists():
        raise FileNotFoundError(f"PDF not found: {path}")
    if file.suffix.lower() != ".pdf":
        raise ValueError("Only .pdf files are supported")
    #2.open the PDF safely 
    try:
        doc = pymupdf.open(file)
    except Exception as e:
        raise ValueError(f"Could not open PDF (corrupt?): {e}")

    if doc.needs_pass:
        raise ValueError("PDF is password-protected")  
    #3.loop all pages and skip empty 
    pages = []
    try:
        for index, page in enumerate(doc):
            text = page.get_text(sort=True).strip()
            if not text:
                reason = "scanned image" if page.get_images() else "blank"
                print(f"Page {index + 1}: skipped ({reason})")
                continue
            pages.append(PageContent(text=text, source=file.name, page=index + 1))
    except Exception as e:
        raise ValueError(f"Error occurred while processing PDF: {e}")
    # 4. close and print if page load fails
    finally:
       doc.close()
    if not pages:
        raise ValueError("No extractable text found (scanned PDF? OCR needed)")
    return pages  

if __name__ == "__main__":
    result = load_pdf("data/full_stack_resume(1).pdf") 
    print(f"Loaded {len(result)} pages")
    print(result[0].source, result[0].page)
    print(result[0].text[:300])
        