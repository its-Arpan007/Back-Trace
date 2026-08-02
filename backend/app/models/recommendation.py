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


class RecommendationModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "recommendations"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    recommendation_type = Column(String(50), nullable=False, index=True) # concept, question, revision, practice, resource, video, article, assessment, challenge, reflection, teacher_intervention
    title = Column(String(250), nullable=False)
    description = Column(Text, nullable=False)
    target_concept_code = Column(String(100), index=True, nullable=False)
    trigger_diagnosis_id = Column(UUID(as_uuid=True), nullable=True)
    priority_score = Column(Float, default=1.0, nullable=False)
    urgency_level = Column(String(50), default="medium", nullable=False) # low, medium, high, critical
    expected_improvement_delta = Column(Float, default=0.15, nullable=False)
    est_duration_minutes = Column(Integer, default=15, nullable=False)
    reasoning_explanation = Column(Text, nullable=False)
    evidence_json = Column(JSON, default=list, nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False)
    is_dismissed = Column(Boolean, default=False, nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)


class RecommendationHistoryModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "recommendation_history"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    recommendation_id = Column(UUID(as_uuid=True), ForeignKey("recommendations.id", ondelete="CASCADE"), nullable=False, index=True)
    action_taken = Column(String(50), nullable=False) # accepted, skipped, completed, ignored


class RecommendationFeedbackModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "recommendation_feedback"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    recommendation_id = Column(UUID(as_uuid=True), ForeignKey("recommendations.id", ondelete="CASCADE"), nullable=False, index=True)
    rating_score = Column(Integer, default=5, nullable=False)
    feedback_text = Column(Text, nullable=True)


class LearningPlanModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "learning_plans"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    plan_type = Column(String(50), nullable=False, index=True) # today, weekly, revision, recovery, exam_prep, fast_recovery, mastery_plan
    plan_title = Column(String(200), nullable=False)
    concepts_sequence_json = Column(JSON, default=list, nullable=False)
    estimated_duration_minutes = Column(Integer, default=45, nullable=False)
    expected_outcome = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)


class DailyLearningPlanModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "daily_learning_plan"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    plan_date = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    tasks_json = Column(JSON, default=list, nullable=False)
    completion_pct = Column(Float, default=0.0, nullable=False)


class WeeklyLearningPlanModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "weekly_learning_plan"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    week_start_date = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    daily_targets_json = Column(JSON, default=dict, nullable=False)
    target_mastery_avg = Column(Float, default=0.85, nullable=False)


class RevisionScheduleModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "revision_schedule"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    concept_code = Column(String(100), index=True, nullable=False)
    scheduled_date = Column(DateTime(timezone=True), nullable=False)
    revision_reason = Column(String(100), nullable=False)
    is_completed = Column(Boolean, default=False, nullable=False)


class ReviewQueueModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "review_queue"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    concept_code = Column(String(100), index=True, nullable=False)
    priority = Column(Float, default=1.0, nullable=False)
    days_overdue = Column(Integer, default=0, nullable=False)


class PracticeQueueModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "practice_queue"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    concept_code = Column(String(100), index=True, nullable=False)
    difficulty = Column(String(50), default="medium", nullable=False)
    bloom_level = Column(String(50), default="apply", nullable=False)


class ResourceRecommendationModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "resource_recommendations"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    resource_id = Column(String(100), nullable=False)
    resource_type = Column(String(50), nullable=False) # video, article, interactive, book, pdf
    title = Column(String(250), nullable=False)
    url = Column(Text, nullable=False)
    difficulty = Column(String(50), default="medium", nullable=False)
    est_minutes = Column(Integer, default=10, nullable=False)
    match_score = Column(Float, default=0.9, nullable=False)


class GoalRecommendationModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "goal_recommendations"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    goal_title = Column(String(200), nullable=False)
    target_mastery = Column(Float, default=0.85, nullable=False)
    target_date = Column(DateTime(timezone=True), nullable=True)


class RecommendationStatisticsModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "recommendation_statistics"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    total_generated = Column(Integer, default=0, nullable=False)
    total_accepted = Column(Integer, default=0, nullable=False)
    total_completed = Column(Integer, default=0, nullable=False)
    completion_rate = Column(Float, default=0.0, nullable=False)
    feedback_avg = Column(Float, default=5.0, nullable=False)


class RecommendationRuleModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "recommendation_rules"

    rule_code = Column(String(100), unique=True, index=True, nullable=False)
    rule_name = Column(String(200), nullable=False)
    condition_json = Column(JSON, nullable=False)
    priority_weight = Column(Float, default=1.0, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
