from typing import List, Dict, Any, Tuple


class ConfidenceEngine:
    """Calculates deterministic 0-100% confidence score with explanation for the diagnosis."""

    def calculate_confidence(
        self,
        matched_rule: Dict[str, Any],
        evidence_records: List[Dict[str, Any]],
        graph_prereqs_count: int,
    ) -> Tuple[float, str]:
        base_confidence = matched_rule.get("confidence_weight", 0.80) * 100.0
        evidence_bonus = min(len(evidence_records) * 3.5, 15.0)
        graph_bonus = min(graph_prereqs_count * 2.0, 10.0)

        final_score = min(base_confidence + evidence_bonus + graph_bonus, 98.5)
        explanation = (
            f"Confidence {final_score:.1f}% derived from rule '{matched_rule.get('rule_code', 'DEFAULT')}' "
            f"({base_confidence:.0f}%), backed by {len(evidence_records)} evidence items (+{evidence_bonus:.1f}%) "
            f"and {graph_prereqs_count} prerequisite graph nodes (+{graph_bonus:.1f}%)."
        )
        return round(final_score, 1), explanation


confidence_engine = ConfidenceEngine()
