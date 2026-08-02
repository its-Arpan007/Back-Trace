from typing import List, Dict, Any


class MisconceptionDetector:
    """Detects specific student misconceptions using question metadata, attempt answer, and graph mappings."""

    def detect_misconceptions(
        self, question: Dict[str, Any], student_answer: Any
    ) -> List[Dict[str, Any]]:
        detected = []
        misconceptions = question.get("misconceptions", [])

        for m in misconceptions:
            code = m.get("misconception_code", "MIS_DEFAULT_01")
            common_mistakes = m.get("common_mistakes_json", []) or m.get("common_student_mistakes", [])

            # Match student answer against known common mistakes
            if str(student_answer).strip().lower() in [str(c).strip().lower() for c in common_mistakes]:
                detected.append({
                    "misconception_code": code,
                    "severity": m.get("severity", "medium"),
                    "evidence": f"Selected option/answer '{student_answer}' matches misconception pattern '{code}'.",
                    "recommended_remediation": m.get("recommended_remediation", ["Interactive visualizer"]),
                })

        if not detected and misconceptions:
            # Fallback to primary misconception if present
            m0 = misconceptions[0]
            detected.append({
                "misconception_code": m0.get("misconception_code", "MIS_CONCEPT_GAP_01"),
                "severity": m0.get("severity", "medium"),
                "evidence": "Pattern mismatch during problem-solving execution.",
                "recommended_remediation": ["Concept revision & practice"],
            })

        return detected


misconception_detector = MisconceptionDetector()
