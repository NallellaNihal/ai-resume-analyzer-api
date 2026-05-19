# AI Resume Analyzer API

A FastAPI-based Resume Analyzer that accepts a resume PDF and a Job Description, extracts resume text, compares it with the job description, generates an ATS-style score, extracts skills, and identifies missing keywords.

## Features

- Upload resume PDF
- Extract text using PyPDF2
- Match resume against Job Description
- Generate ATS score
- Extract technical skills
- Detect missing keywords
- REST API with Swagger UI
- Postman collection included
- Docker support

## Tech Stack

- FastAPI
- PyPDF2
- scikit-learn
- Uvicorn
- Docker
- Postman

## Project Structure

```text
ai-resume-analyzer-api/
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── services/
│   │   ├── analyzer.py
│   │   ├── pdf_parser.py
│   │   └── skill_extractor.py
│   └── utils/
│       └── text_cleaner.py
├── sample_data/
│   └── sample_jd.txt
├── postman/
│   └── AI_Resume_Analyzer_API.postman_collection.json
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Run Locally

### 1. Create virtual environment

```bash
cd ai-resume-analyzer-api
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Start API server

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Health Check

```http
GET /
```

### Analyze Resume

```http
POST /analyze
```

Form-data:

| Key | Type | Required |
|---|---|---|
| resume | File PDF | Yes |
| job_description | Text | Yes |

Example response:

```json
{
  "ats_score": 78.42,
  "match_percentage": 78.42,
  "resume_skills": ["python", "fastapi", "docker"],
  "jd_skills": ["python", "fastapi", "docker", "sql"],
  "matched_skills": ["python", "fastapi", "docker"],
  "missing_skills": ["sql"],
  "missing_keywords": ["database", "api", "deployment"],
  "recommendation": "Good match. Add the missing skills/keywords naturally if you have experience with them."
}
```

## Test Using curl

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
  -F "resume=@/path/to/your/resume.pdf" \
  -F "job_description=$(cat sample_data/sample_jd.txt)"
```

## Test Using Postman

1. Open Postman.
2. Import `postman/AI_Resume_Analyzer_API.postman_collection.json`.
3. Open the `Analyze Resume` request.
4. Go to `Body > form-data`.
5. For `resume`, choose your PDF file.
6. For `job_description`, paste the job description.
7. Send the request.

## Run With Docker

### Build image

```bash
docker build -t ai-resume-analyzer-api .
```

### Run container

```bash
docker run -p 8000:8000 ai-resume-analyzer-api
```

Open:

```text
http://127.0.0.1:8000/docs
```

## GitHub Upload Commands

```bash
cd ai-resume-analyzer-api
git init
git add .
git commit -m "Initial commit: AI Resume Analyzer API"
gh repo create ai-resume-analyzer-api --public --source=. --remote=origin --push
```

## Resume Project Description

**AI Resume Analyzer API** — Built a FastAPI-based resume screening system that extracts text from PDF resumes using PyPDF2, compares resume content with job descriptions using TF-IDF cosine similarity, generates ATS-style match scores, extracts technical skills, and identifies missing keywords to help improve job application relevance. Containerized the project with Docker and tested REST endpoints using Postman.

## Future Improvements

- Add transformer-based semantic matching
- Add authentication
- Store analysis history in SQLite/PostgreSQL
- Add frontend using React or Streamlit
- Export reports as PDF
