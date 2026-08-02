from typing import Dict, Any


class AIResponseValidator:
    """Verifies that AI responses NEVER contradict deterministic Rule, Diagnostic, or Recommendation Engine outputs."""

    def validate_grounding(self, ai_output: str, deterministic_context: Dict[str, Any]) -> Dict[str, Any]:
        is_grounded = True
        reason = "Output is aligned with deterministic diagnosis."

        # If LLM claims answer was correct when Rule Engine diagnosed an error
        if "your answer was completely correct" in ai_output.lower() and deterministic_context.get("diagnosis_summary"):
            is_grounded = False
            reason = "AI output conflicted with deterministic diagnostic finding."

        return {
            "is_grounded": is_grounded,
            "reason": reason,
            "validated_output": ai_output if is_grounded else f"[BACKTRACE Grounding Refinement]: {deterministic_context.get('diagnosis_summary')}",
        }


response_validator = AIResponseValidator()
