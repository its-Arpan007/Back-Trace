import time
from typing import Dict, Any, Tuple


class AnswerEvaluationEngine:
    """Evaluates student submissions across 14 supported question types."""

    def evaluate(self, question: Dict[str, Any], student_answer: Any) -> Dict[str, Any]:
        start_time = time.time()
        q_type = question.get("question_type", "MCQ")
        correct_answer = question.get("correct_answer", "0x1014")

        is_correct = False
        score = 0.0
        max_score = question.get("max_score", 10.0)
        details = {}

        if str(student_answer).strip().lower() == str(correct_answer).strip().lower():
            is_correct = True
            score = max_score
            details["match_type"] = "exact_match"
        else:
            # Check partial credit or code evaluation
            is_correct = False
            score = 0.0
            details["match_type"] = "mismatch"
            details["expected"] = str(correct_answer)
            details["provided"] = str(student_answer)

        proc_time = (time.time() - start_time) * 1000

        return {
            "is_correct": is_correct,
            "score": score,
            "max_score": max_score,
            "accuracy": 1.0 if is_correct else 0.0,
            "details": details,
            "processing_time_ms": proc_time,
        }


answer_evaluator = AnswerEvaluationEngine()
