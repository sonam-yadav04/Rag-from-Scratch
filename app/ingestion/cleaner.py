# import re
# import unicodedata
# import sys
# from app.ingestion.pdf_loader import load_pdf
# #1.patterns, compiled once
# _CONTROL_AND_INVISIBLE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f\u200b-\u200d\ufeff]")
# _SPACES = re.compile(r"[ \t]+")
# _HYPHEN_BREAK = re.compile(r"([a-z])-\n([a-z])")
# _BLANK_RUNS = re.compile(r"\n{3,}")

# #2. normalize unicode and line endings
# text = unicodedata.normalize("NFKC", text)
# text = text.replace("\r\n", "\n").replace("\r", "\n")

# #3. remove noise, in this order
# def clean_text(text: str) -> str:
#     text = _CONTROL_AND_INVISIBLE.sub("", text)
#     text = _SPACES.sub(" ", text)
#     text = "\n".join(line.strip() for line in text.split("\n"))
#     text = _HYPHEN_BREAK.sub(r"\1\2", text)
#     text = _BLANK_RUNS.sub("\n\n", text)
#     return text.strip()

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

import re

def clean_text(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = "\n".join(line.strip() for line in text.split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()