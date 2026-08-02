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


class DiagnosisReportModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "diagnosis_reports"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    concept_code = Column(String(100), index=True, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    score = Column(Float, default=0.0, nullable=False)
    evaluation_details_json = Column(JSON, default=dict, nullable=False)
    primary_root_cause = Column(String(100), nullable=False, index=True)
    secondary_root_causes_json = Column(JSON, default=list, nullable=False)
    confidence_score = Column(Float, default=0.0, nullable=False)
    severity = Column(String(50), default="medium", nullable=False)
    evidence_json = Column(JSON, default=list, nullable=False)
    detected_misconceptions_json = Column(JSON, default=list, nullable=False)
    weak_prerequisites_json = Column(JSON, default=list, nullable=False)
    bloom_level = Column(String(50), default="apply", nullable=False)
    mastery_impact_json = Column(JSON, default=dict, nullable=False)
    recommended_actions_json = Column(JSON, default=list, nullable=False)
    processing_time_ms = Column(Float, default=0.0, nullable=False)
    engine_versions_json = Column(JSON, default=dict, nullable=False)

    evidence_records = relationship("EvidenceRecordModel", back_populates="diagnosis", cascade="all, delete-orphan")


class DiagnosticRuleModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "diagnostic_rules"

    rule_code = Column(String(100), unique=True, index=True, nullable=False)
    rule_type = Column(String(50), nullable=False, index=True) # concept, prerequisite, misconception, pattern, bloom, difficulty, time, confidence
    description = Column(Text, nullable=False)
    condition_json = Column(JSON, nullable=False)
    root_cause_target = Column(String(100), nullable=False)
    confidence_weight = Column(Float, default=0.85, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)


class EvidenceRecordModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "evidence_records"

    diagnosis_id = Column(UUID(as_uuid=True), ForeignKey("diagnosis_reports.id", ondelete="CASCADE"), nullable=False, index=True)
    evidence_source = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    weight = Column(Float, default=1.0, nullable=False)
    details_json = Column(JSON, default=dict, nullable=False)

    diagnosis = relationship("DiagnosisReportModel", back_populates="evidence_records")


class StudentAttemptHistoryModel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "student_attempt_history"

    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    is_correct = Column(Boolean, nullable=False)
    time_spent_seconds = Column(Integer, default=0, nullable=False)
    hints_used = Column(Integer, default=0, nullable=False)
    selected_option = Column(Text, nullable=True)
    error_pattern = Column(String(100), nullable=True)
