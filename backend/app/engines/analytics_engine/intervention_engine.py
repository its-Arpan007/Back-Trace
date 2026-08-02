from typing import Dict, Any, List


class InterventionEngine:
    """Identifies high-risk students, low engagement, rapid decay, and teacher alerts."""

    def evaluate_interventions(
        self,
        student_id: str,
        overall_mastery: float,
        decay_rate: float,
    ) -> Dict[str, Any]:
        needs_intervention = False
        reason = "None"
        priority = "low"

        if overall_mastery < 0.40 or decay_rate > 0.35:
            needs_intervention = True
            reason = "Persistent Prerequisite Failure & Rapid Decay"
            priority = "high"

        return {
            "student_id": student_id,
            "needs_intervention": needs_intervention,
            "intervention_reason": reason,
            "priority": priority,
            "recommended_teacher_action": "Schedule 1-on-1 tutoring session on Array Memory Layout.",
        }


intervention_engine = InterventionEngine()
