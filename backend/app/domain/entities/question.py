from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from app.domain.entities.base import Entity


@dataclass
class QuestionEntity(Entity):
    question_id: str = ""
    concept_id: str = ""
    sub_concept_id: Optional[str] = None
    prerequisites: List[str] = field(default_factory=list)
    prompt: str = ""
    question_type: str = "multiple_choice"
    difficulty: str = "medium"
    bloom_level: str = "apply"  # remember, understand, apply, analyze, evaluate, create
    expected_time_seconds: int = 60
    expected_confidence: float = 0.8
    options: List[str] = field(default_factory=list)
    correct_answer: str = ""
    explanation: Optional[str] = None
    common_mistakes: List[str] = field(default_factory=list)
    misconception_codes: List[str] = field(default_factory=list)
    root_cause_mapping: Dict[str, str] = field(default_factory=dict)
    learning_resources: List[str] = field(default_factory=list)
    hints: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    question_version: str = "1.0.0"
    language: str = "en"
    validation_rules: Dict[str, Any] = field(default_factory=dict)
