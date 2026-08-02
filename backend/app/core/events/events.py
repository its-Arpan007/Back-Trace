from dataclasses import dataclass, field
from typing import Dict, Any, List
from app.core.events.base_event import BaseEvent


@dataclass
class QuestionSubmittedEvent(BaseEvent):
    student_id: str = ""
    question_id: str = ""
    given_answer: str = ""


@dataclass
class DiagnosisCompletedEvent(BaseEvent):
    diagnosis_id: str = ""
    student_id: str = ""
    question_id: str = ""
    diagnosis_type: str = ""
    root_cause: str = ""


@dataclass
class MasteryUpdatedEvent(BaseEvent):
    student_id: str = ""
    concept_id: str = ""
    new_mastery_score: float = 0.0
    mastery_level: str = ""


@dataclass
class RecommendationGeneratedEvent(BaseEvent):
    student_id: str = ""
    recommended_items: List[str] = field(default_factory=list)


@dataclass
class StudentLoggedInEvent(BaseEvent):
    student_id: str = ""
    ip_address: str = ""


@dataclass
class AnalyticsCalculatedEvent(BaseEvent):
    student_id: str = ""
    accuracy: float = 0.0
    metrics: Dict[str, Any] = field(default_factory=dict)
