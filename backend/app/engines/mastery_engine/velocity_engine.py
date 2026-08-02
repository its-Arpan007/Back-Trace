from typing import Dict, Any, List


class LearningVelocityEngine:
    """Calculates learning speed, concept acquisition rate, and difficulty adaptation velocity."""

    def calculate_velocity(
        self,
        attempts_count: int,
        correct_count: int,
        avg_response_time_seconds: float,
    ) -> Dict[str, float]:
        accuracy = correct_count / max(attempts_count, 1)
        speed_factor = max(1.0 - (avg_response_time_seconds / 300.0), 0.2)
        learning_speed = round(accuracy * speed_factor * 1.5, 2)
        acquisition_rate = round(correct_count * 0.75, 2)
        improvement_delta = round(accuracy * 0.10, 2)

        return {
            "learning_speed": learning_speed,
            "concept_acquisition_rate": acquisition_rate,
            "avg_improvement": improvement_delta,
            "recovery_speed": round(learning_speed * 1.1, 2),
        }


velocity_engine = LearningVelocityEngine()
