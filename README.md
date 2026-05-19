# AI Resume Analyzer API with FastAPI, NLP & Streamlit Dashboard

An AI-powered Resume Analyzer built using FastAPI, Streamlit, and scikit-learn that extracts text from PDF resumes, compares resumes against job descriptions using NLP-based TF-IDF cosine similarity, generates ATS-style scores, identifies missing skills and keywords, and visualizes resume analysis using an interactive Streamlit dashboard.

---

## Features

- Upload resume PDF
- Extract text using PyPDF2
- Match resume against Job Description
- Generate ATS-style score
- NLP-based TF-IDF cosine similarity
- Extract technical skills
- Detect missing keywords
- Interactive Streamlit frontend dashboard
- ATS progress visualization
- Skill match pie chart
- Download JSON analysis report
- REST API with Swagger UI
- Postman API testing
- Docker support

---

## Tech Stack

- Python
- FastAPI
- Streamlit
- PyPDF2
- scikit-learn
- Matplotlib
- Uvicorn
- Docker
- Postman

---

## Workflow

```text
Resume PDF Upload
        ↓
PDF Text Extraction (PyPDF2)
        ↓
Text Cleaning & Keyword Extraction
        ↓
TF-IDF Vectorization
        ↓
Cosine Similarity Matching
        ↓
ATS Score Generation
        ↓
Skill & Missing Keyword Analysis
        ↓
Frontend Visualization (Streamlit)
```

---

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
│
├── frontend/
│   └── app.py
│
├── postman/
│   └── AI_Resume_Analyzer_API.postman_collection.json
│
├── sample_data/
│   └── sample_jd.txt
│
├── screenshots/
│   ├── dashboard.png
│   ├── swagger.png
│   └── postman.png
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── LICENSE
└── README.md
```

---

## Screenshots

### Streamlit Dashboard

![Dashboard](screenshots/dashboard.png)

### Swagger API Documentation

![Swagger](screenshots/swagger.png)

### Postman API Testing

![Postman](screenshots/postman.png)

---

# Run Locally

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-analyzer-api.git
cd ai-resume-analyzer-api
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. Start FastAPI Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 5. Start Streamlit Frontend

Open another terminal:

```bash
cd ai-resume-analyzer-api
source venv/bin/activate
streamlit run frontend/app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# API Endpoints

## Health Check

```http
GET /
```

---

## Analyze Resume

```http
POST /analyze
```

### Form Data

| Key | Type | Required |
|---|---|---|
| resume | File PDF | Yes |
| job_description | Text | Yes |

---

## Example Response

```json
{
  "ats_score": 72.87,
  "match_percentage": 9.58,
  "resume_skills": [
    "python",
    "fastapi",
    "docker"
  ],
  "jd_skills": [
    "python",
    "fastapi",
    "docker",
    "sql"
  ],
  "matched_skills": [
    "python",
    "fastapi",
    "docker"
  ],
  "missing_skills": [
    "sql"
  ],
  "missing_keywords": [
    "deployment"
  ],
  "recommendation": "Good match. Your resume matches many requirements but can still be improved."
}
```

---

# Test Using curl

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
  -F "resume=@/path/to/resume.pdf" \
  -F "job_description=$(cat sample_data/sample_jd.txt)"
```

---

# Test Using Postman

1. Open Postman
2. Import the Postman collection
3. Select `POST /analyze`
4. Go to `Body → form-data`
5. Upload resume PDF
6. Paste Job Description
7. Click Send

---

# Run With Docker

## Build Docker Image

```bash
docker build -t ai-resume-analyzer-api .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 ai-resume-analyzer-api
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Fedora Notes

If `scikit-learn` installation fails on Fedora 44 / Python 3.14:

```bash
pip install fastapi uvicorn python-multipart PyPDF2 scikit-learn pydantic
```

---

# GitHub Upload Commands

```bash
git init
git add .
git commit -m "Initial commit: AI Resume Analyzer API"
gh repo create ai-resume-analyzer-api --public --source=. --remote=origin --push
```

---

# Key Functionalities

- REST API using FastAPI
- Interactive Streamlit dashboard
- NLP-based similarity scoring
- Skill extraction engine
- Missing keyword detection
- ATS score visualization
- JSON report export
- Docker container support

---

# Resume Project Description

Built an AI-powered Resume Analyzer using FastAPI, Streamlit, and scikit-learn that extracts text from PDF resumes, compares resumes against job descriptions using NLP-based TF-IDF cosine similarity, generates ATS-style scores, identifies missing skills and keywords, visualizes skill matching using Streamlit dashboards and charts, and supports Dockerized deployment and Postman API testing.

---

# Future Improvements

- Transformer-based semantic matching
- Resume section-wise scoring
- Authentication system
- SQLite/PostgreSQL integration
- PDF report export
- Cloud deployment (AWS/Render/Railway)
- Multi-resume batch analysis

---

# License

This project is licensed under the MIT License.
