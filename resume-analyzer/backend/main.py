from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os
from resume_parser import extract_text_from_pdf
from ai_service import analyze_resume

app = FastAPI(
    title="AI Resume Analyzer",
    description="Analyze resumes against job descriptions using AI"
)

origins = [
    "http://localhost:3000",
    "https://resume-analyzer.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_resume_endpoint(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        content = await resume.read()
        temp_file.write(content)
        temp_path = temp_file.name

    try:
        resume_text = extract_text_from_pdf(temp_path)

        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from PDF")

        result = analyze_resume(resume_text, job_description)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)

@app.get("/")
def read_root():
    return {"message": "AI Resume Analyzer API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}