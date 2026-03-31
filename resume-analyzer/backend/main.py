from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os
from resume_parser import extract_text_from_pdf
from ai_service import analyze_resume

# Create FastAPI app
app = FastAPI(title="AI Resume Analyzer", description="Analyze resumes against job descriptions using AI")

# Add CORS middleware to allow requests from React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_resume_endpoint(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    """
    Endpoint to analyze a resume against a job description.

    - **resume**: PDF file upload of the resume
    - **job_description**: Text of the job description
    """
    # Validate file type
    if not resume.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        content = await resume.read()
        temp_file.write(content)
        temp_path = temp_file.name

    try:
        # Extract text from PDF
        resume_text = extract_text_from_pdf(temp_path)

        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from PDF")

        # Analyze with AI
        result = analyze_resume(resume_text, job_description)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

    finally:
        # Clean up temporary file
        if os.path.exists(temp_path):
            os.unlink(temp_path)

@app.get("/")
def read_root():
    return {"message": "AI Resume Analyzer API"}