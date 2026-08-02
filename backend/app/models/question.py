from datetime import datetime, timezone
import uuid
from sqlalchemy import (
    Column,
    String,
    Boolean,
    DateTime,
    Integer,
    Float,
    ForeignKey,
    JSON,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database.base import Base, UUIDPrimaryKeyMixin, TimestampMixin


class QuestionModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "questions"

    title = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, index=True, nullable=False)
    question_statement = Column(Text, nullable=False)
    question_type = Column(String(50), default="MCQ", nullable=False, index=True) # MCQ, Multiple Select, True False, Fill in the Blank, Short Answer, Long Answer, Code, Code Output, Drag and Drop, Matching, Numerical, Diagram Based, Assertion Reason, Case Study
    difficulty = Column(String(50), default="medium", nullable=False, index=True) # easy, medium, hard, expert
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subjects.id", ondelete="SET NULL"), nullable=True, index=True)
    chapter_id = Column(UUID(as_uuid=True), ForeignKey("chapters.id", ondelete="SET NULL"), nullable=True, index=True)
    topic_id = Column(UUID(as_uuid=True), ForeignKey("topics.id", ondelete="SET NULL"), nullable=True, index=True)
    primary_concept_id = Column(UUID(as_uuid=True), ForeignKey("concepts.id", ondelete="SET NULL"), nullable=True, index=True)
    bloom_level = Column(String(50), default="apply", nullable=False)
    estimated_time_seconds = Column(Integer, default=120, nullable=False)
    expected_accuracy = Column(Float, default=0.75, nullable=False)
    expected_confidence = Column(Float, default=0.70, nullable=False)
    max_score = Column(Float, default=10.0, nullable=False)
    passing_score = Column(Float, default=6.0, nullable=False)
    language = Column(String(10), default="en", nullable=False)
    status = Column(String(50), default="published", nullable=False) # draft, in_review, published, archived
    version = Column(String(20), default="1.0.0", nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    versions = relationship("QuestionVersionModel", back_populates="question", cascade="all, delete-orphan")
    tags = relationship("QuestionTagModel", back_populates="question", cascade="all, delete-orphan")
    hints = relationship("QuestionHintModel", back_populates="question", cascade="all, delete-orphan")
    test_cases = relationship("QuestionTestCaseModel", back_populates="question", cascade="all, delete-orphan")
    evaluation_rules = relationship("QuestionEvaluationRuleModel", back_populates="question", cascade="all, delete-orphan")
    concepts = relationship("QuestionConceptModel", back_populates="question", cascade="all, delete-orphan")
    prerequisites = relationship("QuestionPrerequisiteModel", back_populates="question", cascade="all, delete-orphan")
    objectives = relationship("QuestionLearningObjectiveModel", back_populates="question", cascade="all, delete-orphan")
    misconceptions = relationship("QuestionMisconceptionModel", back_populates="question", cascade="all, delete-orphan")
    root_causes = relationship("QuestionRootCauseModel", back_populates="question", cascade="all, delete-orphan")
    statistics = relationship("QuestionStatisticsModel", back_populates="question", uselist=False, cascade="all, delete-orphan")
    rubrics = relationship("QuestionRubricModel", back_populates="question", cascade="all, delete-orphan")


class QuestionVersionModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_versions"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    version = Column(String(20), nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    changes_summary = Column(Text, nullable=True)
    snapshot_json = Column(JSON, nullable=False)
    approval_status = Column(String(50), default="approved", nullable=False)

    question = relationship("QuestionModel", back_populates="versions")


class QuestionTagModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_tags"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    tag_name = Column(String(100), index=True, nullable=False)

    question = relationship("QuestionModel", back_populates="tags")


class QuestionResourceModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_resources"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    resource_id = Column(UUID(as_uuid=True), ForeignKey("resources.id", ondelete="CASCADE"), nullable=False, index=True)
    difficulty = Column(String(50), default="medium", nullable=False)
    duration_minutes = Column(Integer, default=10, nullable=False)


class QuestionHintModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_hints"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    hint_level = Column(Integer, nullable=False) # 1, 2, 3, 4
    hint_text = Column(Text, nullable=False)
    unlock_rule = Column(String(100), default="on_request", nullable=False)
    penalty_score = Column(Float, default=0.0, nullable=False)

    question = relationship("QuestionModel", back_populates="hints")


class QuestionTestCaseModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_test_cases"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    input_data = Column(Text, nullable=False)
    expected_output = Column(Text, nullable=False)
    is_hidden = Column(Boolean, default=False, nullable=False)
    points = Column(Float, default=1.0, nullable=False)

    question = relationship("QuestionModel", back_populates="test_cases")


class QuestionEvaluationRuleModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_evaluation_rules"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    rule_type = Column(String(50), default="exact_match", nullable=False) # exact_match, rubric, code, regex, range
    correct_answer_json = Column(JSON, nullable=False)
    rubric_json = Column(JSON, default=dict, nullable=False)
    expected_runtime_ms = Column(Integer, default=1000, nullable=False)
    expected_complexity = Column(String(50), default="O(N)", nullable=False)

    question = relationship("QuestionModel", back_populates="evaluation_rules")


class QuestionConceptModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_concepts"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    concept_id = Column(UUID(as_uuid=True), ForeignKey("concepts.id", ondelete="CASCADE"), nullable=False, index=True)
    is_primary = Column(Boolean, default=False, nullable=False)
    relationship_strength = Column(Float, default=1.0, nullable=False)

    question = relationship("QuestionModel", back_populates="concepts")


class QuestionPrerequisiteModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_prerequisites"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    prerequisite_concept_id = Column(UUID(as_uuid=True), ForeignKey("concepts.id", ondelete="CASCADE"), nullable=False, index=True)

    question = relationship("QuestionModel", back_populates="prerequisites")


class QuestionLearningObjectiveModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_learning_objectives"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    objective_text = Column(Text, nullable=False)
    bloom_level = Column(String(50), default="apply", nullable=False)
    skill = Column(String(100), default="problem_solving", nullable=False)
    expected_outcome = Column(Text, nullable=True)
    assessment_type = Column(String(50), default="formative", nullable=False)
    success_criteria = Column(Text, nullable=True)

    question = relationship("QuestionModel", back_populates="objectives")


class QuestionMisconceptionModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_misconceptions"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    misconception_code = Column(String(100), index=True, nullable=False)
    severity = Column(String(50), default="medium", nullable=False)
    common_mistakes_json = Column(JSON, default=list, nullable=False)
    detection_clues_json = Column(JSON, default=list, nullable=False)
    correction_strategy = Column(Text, nullable=True)
    remediation_resources_json = Column(JSON, default=list, nullable=False)

    question = relationship("QuestionModel", back_populates="misconceptions")


class QuestionRootCauseModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_root_causes"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    root_cause_type = Column(String(100), nullable=False) # Concept Gap, Prerequisite Gap, Calculation Error, Reading Error, Logic Error, Pattern Recognition, Memory Recall, Carelessness, Time Pressure, Guessing
    confidence_weight = Column(Float, default=0.8, nullable=False)
    evidence_rules_json = Column(JSON, default=dict, nullable=False)
    priority = Column(Integer, default=1, nullable=False)

    question = relationship("QuestionModel", back_populates="root_causes")


class QuestionDifficultyHistoryModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_difficulty_history"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    previous_difficulty = Column(String(50), nullable=False)
    new_difficulty = Column(String(50), nullable=False)
    reason = Column(Text, nullable=True)


class QuestionStatisticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_statistics"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), unique=True, nullable=False)
    attempts_count = Column(Integer, default=0, nullable=False)
    correct_count = Column(Integer, default=0, nullable=False)
    average_time_seconds = Column(Float, default=0.0, nullable=False)
    drop_off_rate = Column(Float, default=0.0, nullable=False)
    hint_usage_count = Column(Integer, default=0, nullable=False)
    misconception_frequency_json = Column(JSON, default=dict, nullable=False)
    root_cause_frequency_json = Column(JSON, default=dict, nullable=False)
    mastery_gain_avg = Column(Float, default=0.0, nullable=False)

    question = relationship("QuestionModel", back_populates="statistics")


class QuestionAttemptTemplateModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_attempt_templates"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    template_name = Column(String(100), nullable=False)
    template_json = Column(JSON, nullable=False)


class QuestionRubricModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_rubrics"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    criteria = Column(String(200), nullable=False)
    max_points = Column(Float, default=5.0, nullable=False)
    level_descriptions_json = Column(JSON, default=dict, nullable=False)

    question = relationship("QuestionModel", back_populates="rubrics")


class QuestionAttachmentModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_attachments"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    file_name = Column(String(255), nullable=False)
    file_url = Column(Text, nullable=False)
    media_type = Column(String(50), default="image", nullable=False)
