from dataclasses import dataclass, field
from typing import List


@dataclass
class RuleMatch:
    rule_id: str
    rule_name: str
    misconception_code: str
    root_cause: str
    confidence: float = 1.0
    evidence: List[str] = field(default_factory=list)
