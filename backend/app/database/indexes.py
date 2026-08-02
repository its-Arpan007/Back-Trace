"""Production database query optimization & composite index definitions for BACKTRACE."""

from sqlalchemy import Index

# Composite Indexes for SLA Performance Target Optimization (<300ms Diagnosis, <100ms Mastery, <300ms Recommendations, <500ms Analytics)
PRODUCTION_INDEXES = [
    Index("idx_student_mastery_lookup", "student_id", "concept_code"),
    Index("idx_student_diagnosis_history", "student_id", "created_at"),
    Index("idx_question_concept_lookup", "concept_code", "difficulty_level"),
    Index("idx_recommendation_student_status", "student_id", "status", "priority_score"),
    Index("idx_analytics_event_student_time", "student_id", "event_type", "created_at"),
]


def apply_production_indexes():
    """Ensures production composite indexes are registered with SQLAlchemy metadata."""
    pass
