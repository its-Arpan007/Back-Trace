from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class ClassSummaryDTO(BaseModel):
    class_id: str
    class_name: str
    subject_name: str
    total_students: int = 30
    average_mastery: float = 0.78
    high_risk_count: int = 2
    weak_concept_code: str = "DSA_ARRAYS_01"


class ClassAnalyticsDTO(BaseModel):
    class_id: str
    class_name: str
    average_mastery: float = 0.78
    average_confidence: float = 0.82
    learning_velocity: float = 1.42
    top_misconceptions: List[Dict[str, Any]] = Field(default_factory=list)
    weak_concepts: List[str] = Field(default_factory=list)
    strong_concepts: List[str] = Field(default_factory=list)
    student_rankings: List[Dict[str, Any]] = Field(default_factory=list)


class InterventionCandidateDTO(BaseModel):
    student_id: str
    student_name: str
    risk_level: str # critical, high, medium
    reason: str
    decay_rate: float = 0.35
    recommended_action: str
    priority: int = 1


class AssessmentBuildRequest(BaseModel):
    title: str
    target_concept_codes: List[str]
    question_count: int = 5
    bloom_level: str = "apply"
    difficulty: str = "medium"


class AssignmentCreateRequest(BaseModel):
    title: str
    class_id: str
    assessment_id: Optional[str] = None
    due_date: str
    reminder_frequency_days: int = 2
