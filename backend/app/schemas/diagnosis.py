from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class DiagnosisRequest(BaseModel):
    student_id: str
    question_id: str
    student_answer: Any
    time_spent_seconds: int = 60
    hints_used: int = 0


class BatchDiagnosisRequest(BaseModel):
    student_id: str
    submissions: List[DiagnosisRequest]


class EvidenceRecordDTO(BaseModel):
    source: str
    description: str
    weight: float = 1.0
    details: Dict[str, Any] = Field(default_factory=dict)


class DiagnosisReportDTO(BaseModel):
    diagnosis_id: Optional[str] = None
    student_id: str
    question_id: str
    concept_code: str
    is_correct: bool
    score: float
    evaluation_details: Dict[str, Any] = Field(default_factory=dict)
    primary_root_cause: str
    secondary_root_causes: List[str] = Field(default_factory=list)
    confidence_score: float
    severity: str = "medium"
    evidence: List[EvidenceRecordDTO] = Field(default_factory=list)
    detected_misconceptions: List[Dict[str, Any]] = Field(default_factory=list)
    weak_prerequisites: List[str] = Field(default_factory=list)
    bloom_level: str = "apply"
    mastery_impact: Dict[str, Any] = Field(default_factory=dict)
    recommended_actions: List[Dict[str, Any]] = Field(default_factory=list)
    recommended_lessons: List[str] = Field(default_factory=list)
    recommended_questions: List[str] = Field(default_factory=list)
    processing_time_ms: float
    engine_versions: Dict[str, str] = Field(default_factory=dict)
    created_at: Optional[datetime] = None


class ExplainRequest(BaseModel):
    diagnosis_id: str


class ExplanationResponse(BaseModel):
    diagnosis_id: str
    natural_language_explanation: str
    key_takeaways: List[str] = Field(default_factory=list)
    suggested_hint: Optional[str] = None
