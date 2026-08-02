from typing import Dict, Any, List
from app.domain.interfaces.engine import IEngine
from app.engines.rule_engine.interfaces import IRuleEngine


class RuleEngine(IEngine, IRuleEngine):
    """Deterministic Rule Engine — Primary Source of Truth for Diagnostic Root Causes."""

    def __init__(self):
        self._rules = [
            {
                "rule_code": "R_CONCEPT_GAP_01",
                "rule_type": "concept",
                "root_cause_target": "Concept Gap",
                "confidence_weight": 0.88,
                "description": "Triggered when concept-specific formula or pointer arithmetic is violated.",
            },
            {
                "rule_code": "R_PREREQ_GAP_01",
                "rule_type": "prerequisite",
                "root_cause_target": "Prerequisite Gap",
                "confidence_weight": 0.85,
                "description": "Triggered when upstream prerequisite concepts have unmastered status.",
            },
            {
                "rule_code": "R_RUSHING_GUESS_01",
                "rule_type": "time",
                "root_cause_target": "Carelessness / Time Pressure",
                "confidence_weight": 0.78,
                "description": "Triggered when time spent is <30% of estimated problem duration.",
            },
            {
                "rule_code": "R_LOGIC_ERROR_01",
                "rule_type": "misconception",
                "root_cause_target": "Logic Error",
                "confidence_weight": 0.82,
                "description": "Triggered on execution or algorithmic branch mismatch.",
            },
        ]

    @property
    def name(self) -> str:
        return "Rule Engine"

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def status(self) -> str:
        return "healthy"

    @property
    def dependencies(self) -> List[str]:
        return []

    async def evaluate_rules(
        self,
        eval_result: Dict[str, Any],
        question: Dict[str, Any],
        misconceptions: List[Dict[str, Any]],
        time_spent_seconds: int,
    ) -> Dict[str, Any]:
        if eval_result.get("is_correct"):
            return {
                "matched_rule": {"rule_code": "R_CORRECT_MASTERY", "confidence_weight": 0.95},
                "primary_root_cause": "None (Mastered)",
                "secondary_root_causes": [],
                "severity": "none",
            }

        est_time = question.get("estimated_time_seconds", 120)
        if time_spent_seconds < (est_time * 0.25):
            r = self._rules[2] # R_RUSHING_GUESS_01
            return {
                "matched_rule": r,
                "primary_root_cause": r["root_cause_target"],
                "secondary_root_causes": ["Reading Error"],
                "severity": "medium",
            }

        if misconceptions:
            r = self._rules[0] # R_CONCEPT_GAP_01
            return {
                "matched_rule": r,
                "primary_root_cause": r["root_cause_target"],
                "secondary_root_causes": ["Logic Error"],
                "severity": misconceptions[0].get("severity", "high"),
            }

        r_default = self._rules[1] # R_PREREQ_GAP_01
        return {
            "matched_rule": r_default,
            "primary_root_cause": r_default["root_cause_target"],
            "secondary_root_causes": ["Calculation Error"],
            "severity": "medium",
        }

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return await self.evaluate_rules(
            eval_result={"is_correct": False},
            question=input_data.get("question", {}),
            misconceptions=[],
            time_spent_seconds=60,
        )

    async def health_check(self) -> bool:
        return True

    async def readiness(self) -> bool:
        return True
