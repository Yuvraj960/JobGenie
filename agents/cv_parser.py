import os
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text() for page in doc])
        return text.strip()
    except Exception as e:
        print(f"[Error reading {pdf_path}]", e)
        return ""