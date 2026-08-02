from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional
from app.domain.entities.base import Entity


@dataclass
class DiagnosisReport(Entity):
    """Standardized output of BACKTRACE Learning Intelligence Platform."""

    diagnosis_id: str = ""
    student_id: str = ""
    question_id: str = ""
    concept_id: str = ""
    is_correct: bool = False
    diagnosis_type: str = "misconception"
    root_cause: str = ""
    confidence_score: float = 1.0
    severity: str = "medium"  # low, medium, high, critical
    evidence: List[str] = field(default_factory=list)
    detected_misconceptions: List[str] = field(default_factory=list)
    mastery_change: float = 0.0
    recommendation_ids: List[str] = field(default_factory=list)
    processing_time_ms: float = 0.0
    generated_timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    engine_version: str = "1.0.0"
    rule_version: str = "1.0.0"
    ai_version: str = "1.0.0"
    metadata: Dict[str, Any] = field(default_factory=dict)


# For backward compatibility
DiagnosisEntity = DiagnosisReport
