from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class DiagnosticResult:
    diagnosis_id: str
    student_id: str
    question_id: str
    diagnosis_type: str
    root_cause: str
    remediation_steps: List[str] = field(default_factory=list)
    confidence: float = 1.0
