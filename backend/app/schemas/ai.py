from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class AIChatRequest(BaseModel):
    user_id: str
    message: str
    concept_code: Optional[str] = None
    role: str = "student" # student, teacher, admin
    provider: str = "gemini" # gemini, openai, anthropic, ollama


class AIChatResponse(BaseModel):
    reply: str
    grounded_in_diagnosis: bool = True
    context_used: Dict[str, Any] = Field(default_factory=dict)
    suggested_actions: List[str] = Field(default_factory=list)
    processing_time_ms: float = 0.0


class AIExplainRequest(BaseModel):
    concept_code: str
    student_id: Optional[str] = None
    explanation_type: str = "analogy" # analogy, worked_example, mnemonic, summary


class AIStudyPlanRequest(BaseModel):
    student_id: str
    target_date: str
    available_hours_per_day: float = 1.5


class AIGenerateQuestionRequest(BaseModel):
    concept_code: str
    bloom_level: str = "apply"
    difficulty: str = "medium"


class AIReflectionRequest(BaseModel):
    student_id: str
    question_id: str
    answer_given: str
