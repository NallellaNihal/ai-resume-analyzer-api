from pydantic import BaseModel
from typing import List


class AnalysisResponse(BaseModel):
    ats_score: float
    match_percentage: float
    resume_skills: List[str]
    jd_skills: List[str]
    matched_skills: List[str]
    missing_skills: List[str]
    missing_keywords: List[str]
    recommendation: str
