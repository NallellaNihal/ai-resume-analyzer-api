from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import AnalysisResponse
from app.services.pdf_parser import extract_text_from_pdf
from app.services.analyzer import analyze_resume

app = FastAPI(
    title="AI Resume Analyzer API",
    description="Upload a resume PDF and compare it with a job description to generate an ATS-style score.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {
        "message": "AI Resume Analyzer API is running",
        "docs": "http://127.0.0.1:8000/docs",
    }


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
):
    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF resumes are supported.")

    if not job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")

    try:
        resume_text = await extract_text_from_pdf(resume)

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the PDF. Please upload a text-based PDF.",
            )

        result = analyze_resume(resume_text, job_description)
        return result

    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(error)}")
