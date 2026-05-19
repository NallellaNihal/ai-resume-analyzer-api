from app.utils.text_cleaner import normalize_text


SKILL_KEYWORDS = {
    "python", "java", "javascript", "typescript", "c", "c++", "c#", "go", "rust",
    "sql", "mysql", "postgresql", "mongodb", "sqlite",
    "html", "css", "react", "node.js", "express.js", "fastapi", "flask", "django",
    "spring boot", "rest api", "api", "microservices",
    "docker", "kubernetes", "git", "github", "linux", "fedora", "ubuntu",
    "aws", "azure", "gcp", "ci/cd", "jenkins",
    "machine learning", "deep learning", "nlp", "transformers", "pytorch",
    "tensorflow", "scikit-learn", "pandas", "numpy",
    "cybersecurity", "security", "cryptography", "solidity", "blockchain",
    "smart contracts", "formal verification", "testing", "unit testing",
    "postman", "swagger", "oauth", "jwt",
}


def extract_skills(text: str) -> list[str]:
    normalized = normalize_text(text)
    found_skills = []

    for skill in SKILL_KEYWORDS:
        if skill in normalized:
            found_skills.append(skill)

    return sorted(found_skills)
