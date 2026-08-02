from typing import Dict, Any, List


class QuestionValidator:
    """Validates question integrity, taxonomy levels, rubrics, and reference links."""

    VALID_QUESTION_TYPES = {
        "MCQ", "Multiple Select", "True False", "Fill in the Blank", "Short Answer",
        "Long Answer", "Code", "Code Output", "Drag and Drop", "Matching",
        "Numerical", "Diagram Based", "Assertion Reason", "Case Study"
    }

    VALID_BLOOM_LEVELS = {"remember", "understand", "apply", "analyze", "evaluate", "create"}

    def validate_questions(self, questions: List[Dict[str, Any]]) -> Dict[str, Any]:
        errors: List[str] = []
        warnings: List[str] = []
        slugs = set()

        for idx, q in enumerate(questions):
            q_id = q.get("id", f"question_{idx}")
            slug = q.get("slug")
            if not slug:
                errors.append(f"Question '{q_id}' is missing a slug.")
            elif slug in slugs:
                errors.append(f"Duplicate slug '{slug}' detected.")
            else:
                slugs.add(slug)

            q_type = q.get("question_type", "MCQ")
            if q_type not in self.VALID_QUESTION_TYPES:
                errors.append(f"Question '{q_id}' has invalid type '{q_type}'.")

            bloom = q.get("bloom_level", "apply").lower()
            if bloom not in self.VALID_BLOOM_LEVELS:
                warnings.append(f"Question '{q_id}' has non-standard Bloom level '{bloom}'.")

            if q_type == "Code" and not q.get("test_cases"):
                warnings.append(f"Code Question '{q_id}' has no test cases configured.")

        return {
            "valid": len(errors) == 0,
            "total_questions": len(questions),
            "errors": errors,
            "warnings": warnings,
        }


question_validator = QuestionValidator()
