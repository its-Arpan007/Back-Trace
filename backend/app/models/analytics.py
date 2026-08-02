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


class AnalyticsEventModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "analytics_events"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    event_type = Column(String(50), nullable=False, index=True)
    payload_json = Column(JSON, default=dict, nullable=False)


class AnalyticsSnapshotModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "analytics_snapshots"

    snapshot_type = Column(String(50), nullable=False, index=True) # student, teacher, institution, concept, question
    entity_id = Column(String(100), nullable=False, index=True)
    metrics_json = Column(JSON, default=dict, nullable=False)


class StudentAnalyticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "student_analytics"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    learning_progress_pct = Column(Float, default=0.0, nullable=False)
    overall_mastery_avg = Column(Float, default=0.0, nullable=False)
    confidence_trend_score = Column(Float, default=0.8, nullable=False)
    retention_trend_score = Column(Float, default=0.85, nullable=False)
    learning_velocity = Column(Float, default=1.0, nullable=False)
    time_spent_total_minutes = Column(Integer, default=0, nullable=False)
    practice_consistency_score = Column(Float, default=0.9, nullable=False)
    weak_concepts_json = Column(JSON, default=list, nullable=False)
    strong_concepts_json = Column(JSON, default=list, nullable=False)
    recommendation_acceptance_rate = Column(Float, default=0.85, nullable=False)
    goal_progress_pct = Column(Float, default=0.0, nullable=False)
    exam_readiness_score = Column(Float, default=0.75, nullable=False)


class TeacherAnalyticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "teacher_analytics"

    teacher_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    class_performance_avg = Column(Float, default=0.78, nullable=False)
    top_misconceptions_json = Column(JSON, default=list, nullable=False)
    weak_concepts_summary_json = Column(JSON, default=list, nullable=False)
    intervention_candidates_count = Column(Integer, default=0, nullable=False)
    recommendation_success_rate = Column(Float, default=0.88, nullable=False)


class InstitutionAnalyticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "institution_analytics"

    institution_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    total_active_students = Column(Integer, default=150, nullable=False)
    course_completion_rate = Column(Float, default=0.82, nullable=False)
    teacher_performance_score = Column(Float, default=0.90, nullable=False)
    daily_active_users = Column(Integer, default=120, nullable=False)
    platform_retention_rate = Column(Float, default=0.94, nullable=False)
    system_health_pct = Column(Float, default=99.9, nullable=False)


class ConceptAnalyticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "concept_analytics"

    concept_code = Column(String(100), unique=True, index=True, nullable=False)
    avg_mastery = Column(Float, default=0.70, nullable=False)
    avg_confidence = Column(Float, default=0.75, nullable=False)
    failure_rate = Column(Float, default=0.20, nullable=False)
    improvement_rate = Column(Float, default=0.15, nullable=False)
    difficulty_trend = Column(String(50), default="medium", nullable=False)
    decay_rate = Column(Float, default=0.10, nullable=False)
    recovery_rate = Column(Float, default=0.85, nullable=False)


class QuestionAnalyticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "question_analytics"

    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), unique=True, nullable=False)
    attempts_count = Column(Integer, default=0, nullable=False)
    accuracy_rate = Column(Float, default=0.0, nullable=False)
    avg_solve_time_seconds = Column(Float, default=0.0, nullable=False)
    hint_usage_rate = Column(Float, default=0.0, nullable=False)
    drop_off_rate = Column(Float, default=0.05, nullable=False)
    difficulty_index = Column(Float, default=0.50, nullable=False)
    discrimination_index = Column(Float, default=0.45, nullable=False)
    top_misconceptions_json = Column(JSON, default=list, nullable=False)


class RecommendationAnalyticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "recommendation_analytics"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    acceptance_rate = Column(Float, default=0.85, nullable=False)
    completion_rate = Column(Float, default=0.80, nullable=False)
    success_rate = Column(Float, default=0.90, nullable=False)
    avg_improvement_delta = Column(Float, default=0.18, nullable=False)
    resource_effectiveness_score = Column(Float, default=0.92, nullable=False)


class MasteryAnalyticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "mastery_analytics"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    concept_code = Column(String(100), index=True, nullable=False)
    mastery_history_json = Column(JSON, default=list, nullable=False)
    trend_slope = Column(Float, default=0.05, nullable=False)


class DiagnosisAnalyticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "diagnosis_analytics"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    total_diagnoses = Column(Integer, default=0, nullable=False)
    primary_cause_frequencies_json = Column(JSON, default=dict, nullable=False)
    avg_confidence_score = Column(Float, default=90.0, nullable=False)


class LearningSessionAnalyticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "learning_session_analytics"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    total_sessions = Column(Integer, default=0, nullable=False)
    avg_session_duration_minutes = Column(Float, default=25.0, nullable=False)
    avg_questions_per_session = Column(Float, default=5.0, nullable=False)
    accuracy_trend = Column(String(50), default="improving", nullable=False)


class EngagementAnalyticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "engagement_analytics"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    streak_days = Column(Integer, default=7, nullable=False)
    daily_active_time_minutes = Column(Float, default=45.0, nullable=False)
    consistency_index = Column(Float, default=0.95, nullable=False)
    study_frequency_score = Column(Float, default=0.90, nullable=False)


class PredictionAnalyticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "prediction_analytics"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    risk_of_failure = Column(Float, default=0.10, nullable=False)
    exam_readiness = Column(Float, default=0.82, nullable=False)
    predicted_decay_rate = Column(Float, default=0.05, nullable=False)
    expected_mastery_8_days = Column(Float, default=0.90, nullable=False)
    intervention_priority = Column(String(50), default="low", nullable=False)


class PerformanceReportModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "performance_reports"

    report_type = Column(String(50), nullable=False, index=True) # daily, weekly, monthly, concept, student, teacher, institution
    entity_id = Column(String(100), nullable=False, index=True)
    report_title = Column(String(250), nullable=False)
    content_json = Column(JSON, default=dict, nullable=False)
    is_pdf_ready = Column(Boolean, default=True, nullable=False)
