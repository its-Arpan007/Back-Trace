from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class StudentAnalyticsDTO(BaseModel):
    student_id: str
    learning_progress_pct: float = 0.0
    overall_mastery_avg: float = 0.0
    confidence_trend_score: float = 0.80
    retention_trend_score: float = 0.85
    learning_velocity: float = 1.0
    time_spent_total_minutes: int = 0
    practice_consistency_score: float = 0.90
    weak_concepts: List[str] = Field(default_factory=list)
    strong_concepts: List[str] = Field(default_factory=list)
    recommendation_acceptance_rate: float = 0.85
    goal_progress_pct: float = 0.0
    exam_readiness_score: float = 0.75


class TeacherAnalyticsDTO(BaseModel):
    teacher_id: str
    class_performance_avg: float = 0.78
    top_misconceptions: List[Dict[str, Any]] = Field(default_factory=list)
    weak_concepts_summary: List[Dict[str, Any]] = Field(default_factory=list)
    intervention_candidates_count: int = 0
    recommendation_success_rate: float = 0.88


class InstitutionAnalyticsDTO(BaseModel):
    institution_id: str
    total_active_students: int = 150
    course_completion_rate: float = 0.82
    teacher_performance_score: float = 0.90
    daily_active_users: int = 120
    platform_retention_rate: float = 0.94
    system_health_pct: float = 99.9


class ConceptAnalyticsDTO(BaseModel):
    concept_code: str
    avg_mastery: float = 0.70
    avg_confidence: float = 0.75
    failure_rate: float = 0.20
    improvement_rate: float = 0.15
    difficulty_trend: str = "medium"
    decay_rate: float = 0.10
    recovery_rate: float = 0.85


class QuestionAnalyticsDTO(BaseModel):
    question_id: str
    attempts_count: int = 0
    accuracy_rate: float = 0.0
    avg_solve_time_seconds: float = 0.0
    hint_usage_rate: float = 0.0
    drop_off_rate: float = 0.05
    difficulty_index: float = 0.50
    discrimination_index: float = 0.45
    top_misconceptions: List[str] = Field(default_factory=list)


class RecommendationAnalyticsDTO(BaseModel):
    student_id: str
    acceptance_rate: float = 0.85
    completion_rate: float = 0.80
    success_rate: float = 0.90
    avg_improvement_delta: float = 0.18
    resource_effectiveness_score: float = 0.92


class PredictionAnalyticsDTO(BaseModel):
    student_id: str
    risk_of_failure: float = 0.10
    exam_readiness: float = 0.82
    predicted_decay_rate: float = 0.05
    expected_mastery_8_days: float = 0.90
    intervention_priority: str = "low"


class InsightItemDTO(BaseModel):
    insight_id: str
    category: str # progress, gap, trend, recommendation, decay, prediction
    natural_language_statement: str
    what_happened: str
    why_it_happened: str
    emerging_trend: str
    action_to_take: str
    expected_improvement: str


class PerformanceReportDTO(BaseModel):
    report_id: Optional[str] = None
    report_type: str
    entity_id: str
    report_title: str
    content: Dict[str, Any] = Field(default_factory=dict)
    is_pdf_ready: bool = True
    created_at: Optional[datetime] = None


class GenerateAnalyticsRequest(BaseModel):
    student_id: str
