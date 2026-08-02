from typing import Dict, Any, List


class PredictionEngine:
    """Predicts future mastery, failure risk, readiness, and time to mastery (<300ms SLA)."""

    def predict_mastery(
        self,
        current_mastery: float,
        p_know: float,
        trend: str,
        attempts_count: int,
    ) -> Dict[str, Any]:
        trend_multiplier = 1.1 if trend == "improving" else (0.8 if trend == "regressing" else 1.0)
        predicted_mastery = round(min(current_mastery * 1.15 * trend_multiplier, 0.98), 4)

        risk_of_failure = round(max((1.0 - current_mastery) * 0.6, 0.05), 2)
        readiness_score = round(min(current_mastery * 1.1, 1.0), 2)
        est_days = max(int((1.0 - current_mastery) * 14.0), 1)

        return {
            "predicted_mastery": predicted_mastery,
            "readiness_score": readiness_score,
            "risk_of_failure": risk_of_failure,
            "est_time_to_mastery_days": est_days,
            "expected_improvement": round(predicted_mastery - current_mastery, 4),
        }


prediction_engine = PredictionEngine()
