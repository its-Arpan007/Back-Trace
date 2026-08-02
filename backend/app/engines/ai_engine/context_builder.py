import time
from typing import Dict, Any, List


class AIContextBuilder:
    """Builds concise, structured educational context (<100ms SLA)."""

    def build_context(
        self,
        student_id: str,
        concept_code: str = "DSA_ARRAYS_01",
        diagnosis_summary: str = "Omission of element byte size multiplier in offset arithmetic formula.",
        mastery_score: float = 0.65,
    ) -> Dict[str, Any]:
        start_time = time.time()

        ctx = {
            "student_id": student_id,
            "target_concept": concept_code,
            "diagnosis_summary": diagnosis_summary,
            "bkt_mastery_score": mastery_score,
            "weak_prerequisites": ["DSA_COMPARISONS_01"],
            "recommendation": "Interactive Array Offset Visualizer",
            "reflection_history": ["Confused stride length with array length."],
        }

        proc_time = (time.time() - start_time) * 1000
        ctx["context_build_time_ms"] = round(proc_time, 2)
        return ctx


context_builder = AIContextBuilder()
