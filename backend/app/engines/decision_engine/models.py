from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class DecisionOutcome:
    next_action: str  # "retest", "remediate_prerequisite", "advance_level"
    next_lesson_id: Optional[str] = None
    next_question_id: Optional[str] = None
    adjusted_difficulty: str = "medium"
    should_retest: bool = False
    mastery_update_required: bool = True
    recommendation_priority: int = 1
    trigger_analytics: bool = True
