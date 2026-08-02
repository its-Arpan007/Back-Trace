from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class RecommendationDTO(BaseModel):
    recommendation_id: Optional[str] = None
    student_id: str
    recommendation_type: str
    title: str
    description: str
    target_concept_code: str
    priority_score: float = 1.0
    urgency_level: str = "medium"
    expected_improvement_delta: float = 0.15
    est_duration_minutes: int = 15
    reasoning_explanation: str
    evidence: List[Dict[str, Any]] = Field(default_factory=list)
    is_completed: bool = False


class LearningPlanDTO(BaseModel):
    plan_id: Optional[str] = None
    student_id: str
    plan_type: str = "today"
    plan_title: str
    concepts_sequence: List[str] = Field(default_factory=list)
    estimated_duration_minutes: int = 45
    expected_outcome: str
    recommendations: List[RecommendationDTO] = Field(default_factory=list)


class DailyLearningPlanDTO(BaseModel):
    student_id: str
    plan_date: datetime
    tasks: List[Dict[str, Any]] = Field(default_factory=list)
    completion_pct: float = 0.0


class WeeklyLearningPlanDTO(BaseModel):
    student_id: str
    week_start_date: datetime
    daily_targets: Dict[str, Any] = Field(default_factory=dict)
    target_mastery_avg: float = 0.85


class RevisionScheduleDTO(BaseModel):
    student_id: str
    concept_code: str
    scheduled_date: datetime
    revision_reason: str
    is_completed: bool = False


class ResourceRecommendationDTO(BaseModel):
    resource_id: str
    resource_type: str
    title: str
    url: str
    difficulty: str = "medium"
    est_minutes: int = 10
    match_score: float = 0.95


class QuestionRecommendationDTO(BaseModel):
    question_id: str
    concept_code: str
    question_statement: str
    difficulty: str = "medium"
    bloom_level: str = "apply"
    recommendation_reason: str


class GoalRecommendationDTO(BaseModel):
    goal_title: str
    target_mastery: float = 0.85
    target_date: Optional[datetime] = None
    reasoning: str


class RecommendationFeedbackRequest(BaseModel):
    student_id: str
    recommendation_id: str
    rating_score: int = 5
    feedback_text: Optional[str] = None
    action_taken: str = "accepted" # accepted, skipped, completed, ignored


class GenerateRecommendationsRequest(BaseModel):
    student_id: str
    focus_concept_code: Optional[str] = None
