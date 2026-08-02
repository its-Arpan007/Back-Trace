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


class ConceptMasteryModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "concept_mastery"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    concept_code = Column(String(100), index=True, nullable=False)
    current_mastery = Column(Float, default=0.0, nullable=False)
    previous_mastery = Column(Float, default=0.0, nullable=False)
    confidence = Column(Float, default=0.70, nullable=False)
    retention_score = Column(Float, default=1.0, nullable=False)
    knowledge_decay = Column(Float, default=0.0, nullable=False)
    attempts_count = Column(Integer, default=0, nullable=False)
    correct_count = Column(Integer, default=0, nullable=False)
    incorrect_count = Column(Integer, default=0, nullable=False)
    avg_response_time_seconds = Column(Float, default=0.0, nullable=False)
    hint_usage_count = Column(Integer, default=0, nullable=False)
    misconceptions_json = Column(JSON, default=list, nullable=False)
    last_practiced = Column(DateTime(timezone=True), nullable=True)
    next_recommended_review = Column(DateTime(timezone=True), nullable=True)
    learning_velocity = Column(Float, default=1.0, nullable=False)
    recovery_progress = Column(Float, default=1.0, nullable=False)
    mastery_trend = Column(String(50), default="improving", nullable=False) # improving, plateau, regressing, recovering
    
    # Bayesian Knowledge Tracing (BKT) Parameters
    p_know = Column(Float, default=0.20, nullable=False) # P(L0) or P(Lt)
    p_transit = Column(Float, default=0.15, nullable=False) # P(T)
    p_slip = Column(Float, default=0.10, nullable=False) # P(S)
    p_guess = Column(Float, default=0.20, nullable=False) # P(G)
    
    deleted_at = Column(DateTime(timezone=True), nullable=True)


class ConceptHistoryModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "concept_history"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    concept_code = Column(String(100), index=True, nullable=False)
    mastery_before = Column(Float, nullable=False)
    mastery_after = Column(Float, nullable=False)
    change_reason = Column(String(100), nullable=False)


class LearningSessionModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "learning_sessions"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    session_start = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    session_end = Column(DateTime(timezone=True), nullable=True)
    duration_seconds = Column(Integer, default=0, nullable=False)
    questions_solved = Column(Integer, default=0, nullable=False)
    accuracy = Column(Float, default=0.0, nullable=False)
    concepts_covered_json = Column(JSON, default=list, nullable=False)
    avg_confidence = Column(Float, default=0.0, nullable=False)
    avg_difficulty = Column(String(50), default="medium", nullable=False)


class LearningEventModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "learning_events"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    event_type = Column(String(50), nullable=False, index=True) # question_attempt, diagnosis, mastery_update, recommendation, reflection, session, review, assessment
    payload_json = Column(JSON, default=dict, nullable=False)


class LearningVelocityModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "learning_velocity"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    learning_speed = Column(Float, default=1.0, nullable=False)
    concept_acquisition_rate = Column(Float, default=1.0, nullable=False) # concepts per week
    avg_improvement = Column(Float, default=0.05, nullable=False)
    recovery_speed = Column(Float, default=1.0, nullable=False)
    difficulty_adaptation = Column(Float, default=1.0, nullable=False)


class KnowledgeDecayModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "knowledge_decay"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    concept_code = Column(String(100), index=True, nullable=False)
    retention_half_life_days = Column(Float, default=14.0, nullable=False)
    days_since_practice = Column(Float, default=0.0, nullable=False)
    predicted_retention = Column(Float, default=1.0, nullable=False)
    review_scheduled_date = Column(DateTime(timezone=True), nullable=True)


class MasterySnapshotModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "mastery_snapshots"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    snapshot_date = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    mastery_map_json = Column(JSON, default=dict, nullable=False)
    overall_mastery_avg = Column(Float, default=0.0, nullable=False)


class MasteryPredictionModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "mastery_predictions"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    concept_code = Column(String(100), index=True, nullable=False)
    predicted_mastery = Column(Float, nullable=False)
    readiness_score = Column(Float, default=0.8, nullable=False)
    risk_of_failure = Column(Float, default=0.1, nullable=False)
    est_time_to_mastery_days = Column(Integer, default=7, nullable=False)
    expected_improvement = Column(Float, default=0.15, nullable=False)


class StudentStatisticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "student_statistics"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    total_questions_solved = Column(Integer, default=0, nullable=False)
    overall_accuracy = Column(Float, default=0.0, nullable=False)
    current_streak_days = Column(Integer, default=0, nullable=False)
    longest_streak_days = Column(Integer, default=0, nullable=False)
    study_frequency_score = Column(Float, default=1.0, nullable=False)
    consistency_score = Column(Float, default=1.0, nullable=False)


class LearningGoalModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "learning_goals"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    goal_title = Column(String(200), nullable=False)
    target_mastery = Column(Float, default=0.85, nullable=False)
    target_date = Column(DateTime(timezone=True), nullable=True)
    current_progress = Column(Float, default=0.0, nullable=False)
    completion_pct = Column(Float, default=0.0, nullable=False)
    remaining_concepts_json = Column(JSON, default=list, nullable=False)


class LearningStreakModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "learning_streaks"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    current_streak = Column(Integer, default=0, nullable=False)
    longest_streak = Column(Integer, default=0, nullable=False)
    last_activity_date = Column(DateTime(timezone=True), nullable=True)
