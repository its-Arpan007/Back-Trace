from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class ConceptMasteryDTO(BaseModel):
    student_id: str
    concept_code: str
    current_mastery: float
    previous_mastery: float = 0.0
    confidence: float = 0.70
    retention_score: float = 1.0
    knowledge_decay: float = 0.0
    attempts_count: int = 0
    correct_count: int = 0
    incorrect_count: int = 0
    avg_response_time_seconds: float = 0.0
    hint_usage_count: int = 0
    misconceptions: List[str] = Field(default_factory=list)
    last_practiced: Optional[datetime] = None
    next_recommended_review: Optional[datetime] = None
    learning_velocity: float = 1.0
    recovery_progress: float = 1.0
    mastery_trend: str = "improving"
    p_know: float = 0.20
    p_transit: float = 0.15
    p_slip: float = 0.10
    p_guess: float = 0.20


class StudentMasterySummaryDTO(BaseModel):
    student_id: str
    overall_mastery_avg: float
    concepts_mastered_count: int
    concepts_in_progress_count: int
    total_concepts_count: int
    current_streak_days: int = 0
    overall_accuracy: float = 0.0
    concept_masteries: List[ConceptMasteryDTO] = Field(default_factory=list)


class TimelinePointDTO(BaseModel):
    day_label: str
    date: datetime
    mastery_score: float
    event_summary: str


class LearningTimelineDTO(BaseModel):
    student_id: str
    concept_code: str
    timeline: List[TimelinePointDTO] = Field(default_factory=list)


class MasteryPredictionDTO(BaseModel):
    student_id: str
    concept_code: str
    predicted_mastery: float
    readiness_score: float = 0.8
    risk_of_failure: float = 0.1
    est_time_to_mastery_days: int = 7
    expected_improvement: float = 0.15


class RecalculateMasteryRequest(BaseModel):
    student_id: str
    concept_code: Optional[str] = None


class GoalDTO(BaseModel):
    goal_id: Optional[str] = None
    goal_title: str
    target_mastery: float = 0.85
    target_date: Optional[datetime] = None
    current_progress: float = 0.0
    completion_pct: float = 0.0


class VelocityDTO(BaseModel):
    student_id: str
    learning_speed: float = 1.0
    concept_acquisition_rate: float = 1.0
    avg_improvement: float = 0.05
    recovery_speed: float = 1.0


class DecayDTO(BaseModel):
    student_id: str
    concept_code: str
    retention_half_life_days: float = 14.0
    days_since_practice: float = 0.0
    predicted_retention: float = 1.0
