from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.services.skill_extractor import extract_skills
from app.utils.text_cleaner import extract_keywords, normalize_text


def calculate_similarity(resume_text: str, job_description: str) -> float:
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2),
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(float(similarity * 100), 2)


def get_missing_keywords(
    resume_text: str,
    job_description: str
) -> list[str]:

    resume_normalized = normalize_text(resume_text)
    jd_keywords = extract_keywords(job_description)

    missing = []

    for keyword in jd_keywords:
        if keyword not in resume_normalized:
            if keyword not in missing:
                missing.append(keyword)

    return missing[:20]


def build_recommendation(
    score: float,
    missing_skills: list[str],
    missing_keywords: list[str]
) -> str:

    if score >= 80:
        base = (
            "Strong match. Your resume is highly aligned "
            "with the job description."
        )

    elif score >= 60:
        base = (
            "Good match. Your resume matches many requirements "
            "but can still be improved."
        )

    elif score >= 40:
        base = (
            "Average match. Add more relevant skills, tools, "
            "and keywords from the job description."
        )

    else:
        base = (
            "Low match. Tailor your resume more closely "
            "to the job description."
        )

    if missing_skills:
        base += (
            f" Consider adding these skills if you have "
            f"experience: {', '.join(missing_skills[:6])}."
        )

    if missing_keywords:
        base += (
            f" Also review missing keywords like: "
            f"{', '.join(missing_keywords[:6])}."
        )

    return base


def analyze_resume(
    resume_text: str,
    job_description: str
) -> dict:

    match_percentage = calculate_similarity(
        resume_text,
        job_description
    )

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    matched_skills = sorted(
        set(resume_skills).intersection(set(jd_skills))
    )

    missing_skills = sorted(
        set(jd_skills).difference(set(resume_skills))
    )

    missing_keywords = get_missing_keywords(
        resume_text,
        job_description
    )

    skill_score = 0

    if jd_skills:
        skill_score = (
            len(matched_skills) / len(jd_skills)
        ) * 100

    ats_score = round(
        (match_percentage * 0.30) +
        (skill_score * 0.70),
        2
    )

    return {
        "ats_score": ats_score,
        "match_percentage": match_percentage,
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "missing_keywords": missing_keywords,
        "recommendation": build_recommendation(
            ats_score,
            missing_skills,
            missing_keywords
        ),
    }
