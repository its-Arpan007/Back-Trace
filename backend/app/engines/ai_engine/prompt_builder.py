import time
from typing import Dict, Any


class AIPromptBuilder:
    """Generates grounded prompt templates (<50ms SLA)."""

    def build_student_coach_prompt(self, message: str, context: Dict[str, Any]) -> str:
        start_time = time.time()
        concept = context.get("target_concept", "DSA_ARRAYS_01")
        diag = context.get("diagnosis_summary", "")

        prompt = (
            f"You are the BACKTRACE AI Learning Coach. "
            f"Grounding Context:\n"
            f"- Concept: {concept}\n"
            f"- Rule Engine Diagnosis: {diag}\n"
            f"- Student Question: {message}\n"
            f"Instructions: Provide a clear, supportive, and pedagogical answer explaining why the diagnosis is correct. Never contradict the diagnosis."
        )
        return prompt


prompt_builder = AIPromptBuilder()
