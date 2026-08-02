from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class QuestionHintSchema(BaseModel):
    id: Optional[str] = None
    hint_level: int
    hint_text: str
    unlock_rule: str = "on_request"
    penalty_score: float = 0.0


class QuestionTestCaseSchema(BaseModel):
    id: Optional[str] = None
    input_data: str
    expected_output: str
    is_hidden: bool = False
    points: float = 1.0


class QuestionMisconceptionMapSchema(BaseModel):
    id: Optional[str] = None
    misconception_code: str
    severity: str = "medium"
    common_mistakes: List[str] = Field(default_factory=list)
    detection_clues: List[str] = Field(default_factory=list)
    correction_strategy: Optional[str] = None
    remediation_resources: List[str] = Field(default_factory=list)


class QuestionRootCauseMapSchema(BaseModel):
    id: Optional[str] = None
    root_cause_type: str
    confidence_weight: float = 0.8
    evidence_rules: Dict[str, Any] = Field(default_factory=dict)
    priority: int = 1


class QuestionStatisticsSchema(BaseModel):
    attempts_count: int = 0
    correct_count: int = 0
    average_time_seconds: float = 0.0
    drop_off_rate: float = 0.0
    hint_usage_count: int = 0
    misconception_frequency: Dict[str, int] = Field(default_factory=dict)
    root_cause_frequency: Dict[str, int] = Field(default_factory=dict)
    mastery_gain_avg: float = 0.0


class QuestionSchema(BaseModel):
    id: Optional[str] = None
    title: str
    slug: str
    question_statement: str
    question_type: str = "MCQ"
    difficulty: str = "medium"
    subject_id: Optional[str] = None
    chapter_id: Optional[str] = None
    topic_id: Optional[str] = None
    primary_concept_id: Optional[str] = None
    secondary_concept_ids: List[str] = Field(default_factory=list)
    prerequisite_concept_ids: List[str] = Field(default_factory=list)
    bloom_level: str = "apply"
    estimated_time_seconds: int = 120
    expected_accuracy: float = 0.75
    expected_confidence: float = 0.70
    max_score: float = 10.0
    passing_score: float = 6.0
    language: str = "en"
    status: str = "published"
    version: str = "1.0.0"
    tags: List[str] = Field(default_factory=list)
    hints: List[QuestionHintSchema] = Field(default_factory=list)
    test_cases: List[QuestionTestCaseSchema] = Field(default_factory=list)
    misconceptions: List[QuestionMisconceptionMapSchema] = Field(default_factory=list)
    root_causes: List[QuestionRootCauseMapSchema] = Field(default_factory=list)
    statistics: Optional[QuestionStatisticsSchema] = None
    created_at: Optional[datetime] = None


class QuestionCreateRequest(BaseModel):
    title: str
    slug: str
    question_statement: str
    question_type: str = "MCQ"
    difficulty: str = "medium"
    subject_id: Optional[str] = None
    chapter_id: Optional[str] = None
    topic_id: Optional[str] = None
    primary_concept_id: Optional[str] = None
    secondary_concept_ids: List[str] = Field(default_factory=list)
    prerequisite_concept_ids: List[str] = Field(default_factory=list)
    bloom_level: str = "apply"
    estimated_time_seconds: int = 120
    tags: List[str] = Field(default_factory=list)
    hints: List[QuestionHintSchema] = Field(default_factory=list)
    test_cases: List[QuestionTestCaseSchema] = Field(default_factory=list)
    misconceptions: List[QuestionMisconceptionMapSchema] = Field(default_factory=list)
    root_causes: List[QuestionRootCauseMapSchema] = Field(default_factory=list)


class QuestionValidationReportDTO(BaseModel):
    valid: bool
    total_questions: int
    errors: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)


class PracticeSetRequest(BaseModel):
    student_id: Optional[str] = None
    concept_codes: List[str] = Field(default_factory=list)
    difficulty: str = "medium"
    question_count: int = 5
    adaptive: bool = True
