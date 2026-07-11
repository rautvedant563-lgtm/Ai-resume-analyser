import fitz  # PyMuPDF
from analyse_pdf import analyse_resume_gemini
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def extract_text_from_resume(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text


def main():
    pdf_path ="vedant_resume.pdf"

    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found: {pdf_path}")
        return

    resume_content = extract_text_from_resume(pdf_path)

    print("Resume Text:\n")
    print(resume_content)

    job_description = """
     
     We are hiring a Python Backend Developer with experience in:

- Flask or Django
- REST API Development
- PostgreSQL or MySQL
- Docker (optional)
- AWS or Cloud Deployment (preferred)
"""

    result = analyse_resume_gemini(resume_content, job_description)

    print("\nResume Analysis:\n")
    print(result)


if __name__ == "__main__":
    main()