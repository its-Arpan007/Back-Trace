from typing import List, Dict, Any


class EvidenceEngine:
    """Collects supporting evidence from current submission, attempt history, time, and hint usage."""

    def collect_evidence(
        self,
        eval_result: Dict[str, Any],
        question: Dict[str, Any],
        student_history: List[Dict[str, Any]],
        time_spent_seconds: int,
        hints_used: int,
    ) -> List[Dict[str, Any]]:
        evidence: List[Dict[str, Any]] = []

        # Current submission evidence
        if not eval_result["is_correct"]:
            evidence.append({
                "source": "Current Submission",
                "description": f"Submitted answer '{eval_result['details'].get('provided')}' mismatched expected '{eval_result['details'].get('expected')}'.",
                "weight": 1.0,
                "details": eval_result["details"],
            })

        # Time-based evidence
        est_time = question.get("estimated_time_seconds", 120)
        if time_spent_seconds < (est_time * 0.3):
            evidence.append({
                "source": "Time Analysis",
                "description": f"Answer submitted in {time_spent_seconds}s (estimated {est_time}s), indicating potential rushing or guessing.",
                "weight": 0.75,
                "details": {"time_spent": time_spent_seconds, "estimated": est_time},
            })
        elif time_spent_seconds > (est_time * 2.5):
            evidence.append({
                "source": "Time Analysis",
                "description": f"Answer took {time_spent_seconds}s (estimated {est_time}s), indicating struggle under time pressure.",
                "weight": 0.70,
                "details": {"time_spent": time_spent_seconds, "estimated": est_time},
            })

        # Hint usage evidence
        if hints_used > 0:
            evidence.append({
                "source": "Hint Usage",
                "description": f"Student requested {hints_used} hint(s) before submitting.",
                "weight": 0.65,
                "details": {"hints_used": hints_used},
            })

        # History evidence
        if student_history:
            recent_fails = sum(1 for h in student_history if not h.get("is_correct", False))
            if recent_fails >= 2:
                evidence.append({
                    "source": "Historical Performance",
                    "description": f"Student has failed {recent_fails} of the last {len(student_history)} questions.",
                    "weight": 0.85,
                    "details": {"recent_fails": recent_fails},
                })

        return evidence


evidence_engine = EvidenceEngine()
