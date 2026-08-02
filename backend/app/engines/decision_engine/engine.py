from typing import Dict, Any, List
from app.domain.interfaces.engine import IEngine
from app.engines.decision_engine.interfaces import IDecisionEngine
from app.engines.decision_engine.models import DecisionOutcome
from app.engines.decision_engine.utils import determine_difficulty_adjustment


class DecisionEngine(IEngine, IDecisionEngine):
    """Decision Engine acting as the operational brain converting diagnosis results into learning actions."""

    @property
    def name(self) -> str:
        return "Decision Engine"

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def status(self) -> str:
        return "healthy"

    @property
    def dependencies(self) -> List[str]:
        return ["Diagnostic Engine", "Mastery Engine"]

    async def make_decision(self, diagnosis_result: Dict[str, Any]) -> Dict[str, Any]:
        is_correct = diagnosis_result.get("is_correct", False)
        current_diff = diagnosis_result.get("difficulty", "medium")
        adjusted_diff = determine_difficulty_adjustment(current_diff, is_correct)

        outcome = DecisionOutcome(
            next_action="remediate_prerequisite" if not is_correct else "advance_level",
            next_lesson_id="LES_ARRAYS_02" if is_correct else "LES_PREREQ_01",
            next_question_id="Q_DSA_002" if is_correct else "Q_PREREQ_001",
            adjusted_difficulty=adjusted_diff,
            should_retest=not is_correct,
            mastery_update_required=True,
            recommendation_priority=10 if not is_correct else 1,
            trigger_analytics=True,
        )

        return {
            "next_action": outcome.next_action,
            "next_lesson_id": outcome.next_lesson_id,
            "next_question_id": outcome.next_question_id,
            "adjusted_difficulty": outcome.adjusted_difficulty,
            "should_retest": outcome.should_retest,
            "mastery_update_required": outcome.mastery_update_required,
            "recommendation_priority": outcome.recommendation_priority,
            "trigger_analytics": outcome.trigger_analytics,
        }

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return await self.make_decision(input_data)

    async def health_check(self) -> bool:
        return True

    async def readiness(self) -> bool:
        return True
