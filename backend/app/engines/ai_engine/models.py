from dataclasses import dataclass, field
from typing import List


@dataclass
class AIExplanationResult:
    explanation_text: str
    hint: str
    personalized_summary: str
    suggested_resources: List[str] = field(default_factory=list)
