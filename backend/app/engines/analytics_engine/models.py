from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class AnalyticsSummary:
    student_id: str
    total_questions: int
    accuracy_rate: float
    metrics: Dict[str, Any] = field(default_factory=dict)
