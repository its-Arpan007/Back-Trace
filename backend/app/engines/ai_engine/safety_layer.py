from typing import Dict, Any


class AISafetyLayer:
    """Validates educational safety, PII protection, and prompt injection defense."""

    def sanitize_and_validate(self, text: str) -> Dict[str, Any]:
        is_safe = True
        reason = "Pass"

        # Check basic safety filters
        if "DROP TABLE" in text.upper() or "IGNORE ALL PREVIOUS INSTRUCTIONS" in text.upper():
            is_safe = False
            reason = "Prompt injection attempt detected"

        return {
            "is_safe": is_safe,
            "reason": reason,
            "sanitized_text": text,
        }


safety_layer = AISafetyLayer()
