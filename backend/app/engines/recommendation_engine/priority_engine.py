from typing import Dict, Any, List


class PriorityEngine:
    """Calculates multi-factor priority score considering weak concepts, prerequisite DAG importance, decay, and urgency."""

    def calculate_priority(
        self,
        concept_code: str,
        mastery_score: float,
        is_prereq: bool,
        knowledge_decay: float,
    ) -> Dict[str, Any]:
        base_priority = (1.0 - mastery_score) * 100.0
        prereq_weight = 25.0 if is_prereq else 0.0
        decay_weight = knowledge_decay * 20.0

        total_score = round(base_priority + prereq_weight + decay_weight, 1)

        urgency = "low"
        if total_score >= 80.0:
            urgency = "critical"
        elif total_score >= 60.0:
            urgency = "high"
        elif total_score >= 40.0:
            urgency = "medium"

        return {
            "concept_code": concept_code,
            "priority_score": total_score,
            "urgency_level": urgency,
            "explanation": f"Priority {total_score} computed from mastery gap ({(1.0-mastery_score)*100:.0f}%), prerequisite weight (+{prereq_weight:.0f}), and decay (+{decay_weight:.1f}).",
        }


priority_engine = PriorityEngine()
