from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class LearningObjectiveSchema(BaseModel):
    id: Optional[str] = None
    objective: str
    bloom_level: str = "apply"
    expected_outcome: Optional[str] = None
    success_criteria: Optional[str] = None


class MisconceptionSchema(BaseModel):
    id: Optional[str] = None
    misconception_code: str
    description: str
    severity: str = "medium"
    common_student_mistakes: List[str] = Field(default_factory=list)
    detection_hints: List[str] = Field(default_factory=list)
    recommended_remediation: List[str] = Field(default_factory=list)


class ResourceSchema(BaseModel):
    id: Optional[str] = None
    title: str
    resource_type: str = "article"
    url: str
    difficulty: str = "medium"
    duration_minutes: int = 10
    language: str = "en"
    provider: str = "BACKTRACE"


class ConceptSchema(BaseModel):
    id: Optional[str] = None
    topic_id: str
    concept_code: str
    title: str
    description: Optional[str] = None
    difficulty: str = "medium"
    bloom_level: str = "apply"
    estimated_learning_time_minutes: int = 30
    mastery_threshold: float = 0.85
    expected_accuracy: float = 0.80
    expected_confidence: float = 0.75
    learning_objective_count: int = 1
    status: str = "active"
    version: str = "1.0.0"
    created_at: Optional[datetime] = None
    objectives: List[LearningObjectiveSchema] = Field(default_factory=list)
    misconceptions: List[MisconceptionSchema] = Field(default_factory=list)
    resources: List[ResourceSchema] = Field(default_factory=list)


class ConceptCreateRequest(BaseModel):
    topic_id: str
    concept_code: str
    title: str
    description: Optional[str] = None
    difficulty: str = "medium"
    bloom_level: str = "apply"
    estimated_learning_time_minutes: int = 30
    mastery_threshold: float = 0.85
    objectives: List[LearningObjectiveSchema] = Field(default_factory=list)
    misconceptions: List[MisconceptionSchema] = Field(default_factory=list)
    resources: List[ResourceSchema] = Field(default_factory=list)


class TopicSchema(BaseModel):
    id: Optional[str] = None
    chapter_id: str
    name: str
    description: Optional[str] = None
    order: int = 1
    difficulty: str = "medium"
    version: str = "1.0.0"
    concepts: List[ConceptSchema] = Field(default_factory=list)


class TopicCreateRequest(BaseModel):
    chapter_id: str
    name: str
    description: Optional[str] = None
    order: int = 1
    difficulty: str = "medium"


class ChapterSchema(BaseModel):
    id: Optional[str] = None
    subject_id: str
    name: str
    description: Optional[str] = None
    order: int = 1
    estimated_hours: float = 1.0
    difficulty: str = "medium"
    version: str = "1.0.0"
    topics: List[TopicSchema] = Field(default_factory=list)


class ChapterCreateRequest(BaseModel):
    subject_id: str
    name: str
    description: Optional[str] = None
    order: int = 1
    estimated_hours: float = 1.0
    difficulty: str = "medium"


class SubjectSchema(BaseModel):
    id: Optional[str] = None
    name: str
    code: str
    description: Optional[str] = None
    icon: str = "book"
    color: str = "#14B8A6"
    difficulty_scale: str = "standard"
    status: str = "active"
    version: str = "1.0.0"
    created_at: Optional[datetime] = None
    chapters: List[ChapterSchema] = Field(default_factory=list)


class SubjectCreateRequest(BaseModel):
    name: str
    code: str
    description: Optional[str] = None
    icon: str = "book"
    color: str = "#14B8A6"
    difficulty_scale: str = "standard"
