import re


STOPWORDS = {
    "a", "an", "the", "and", "or", "to", "for", "of", "in", "on", "with", "as",
    "is", "are", "was", "were", "be", "by", "this", "that", "from", "at", "it",
    "you", "your", "we", "our", "will", "can", "should", "must", "have", "has",
    "experience", "work", "team", "role", "candidate", "job", "description",
    "looking", "experience.", "seeking", "motivated", "enthusiastic",
}


def normalize_text(text: str) -> str:
    text = text.lower()
    text = text.replace("nodejs", "node.js")
    text = text.replace("expressjs", "express.js")
    text = text.replace("scikit learn", "scikit-learn")
    text = re.sub(r"[^a-z0-9+#./-]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_keywords(text: str, limit: int = 40) -> list[str]:
    normalized = normalize_text(text)
    words = normalized.split()

    keywords = []
    for word in words:
        if len(word) < 3:
            continue
        if word in STOPWORDS:
            continue
        if word not in keywords:
            keywords.append(word)

    return keywords[:limit]
