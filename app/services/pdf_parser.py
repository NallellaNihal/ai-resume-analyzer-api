from io import BytesIO
from fastapi import UploadFile
from PyPDF2 import PdfReader


async def extract_text_from_pdf(file: UploadFile) -> str:
    contents = await file.read()
    pdf_stream = BytesIO(contents)
    reader = PdfReader(pdf_stream)

    extracted_pages = []

    for page in reader.pages:
        text = page.extract_text() or ""
        extracted_pages.append(text)

    return "\n".join(extracted_pages)
