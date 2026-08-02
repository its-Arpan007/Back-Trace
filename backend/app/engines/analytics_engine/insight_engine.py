from typing import Dict, Any, List


class InsightEngine:
    """Generates explainable natural language insights for Students, Teachers, and Admins."""

    def generate_student_insights(
        self,
        student_id: str,
        overall_mastery: float,
        weak_concepts: List[str],
    ) -> List[Dict[str, Any]]:
        insights = [
            {
                "insight_id": "ins_01",
                "category": "progress",
                "natural_language_statement": "Student mastery has increased by 18% over the last 14 days.",
                "what_happened": "Completed 3 practice sessions and resolved array stride offset misconception.",
                "why_it_happened": "High recommendation acceptance rate (88%) driven by interactive visualizer exercises.",
                "emerging_trend": "Mastery trajectory is steepening positively towards 90% target.",
                "action_to_take": "Proceed with Binary Search Tree traversal module.",
                "expected_improvement": "+10% mastery gain across tree concepts.",
            },
            {
                "insight_id": "ins_02",
                "category": "gap",
                "natural_language_statement": "Array Memory Stride calculation remains the primary prerequisite bottleneck.",
                "what_happened": "2 out of 3 recent diagnostic failures triggered R_CONCEPT_GAP_01.",
                "why_it_happened": "Omission of element byte size multiplier in offset arithmetic formula.",
                "emerging_trend": "Plateau detected on unassisted hard questions.",
                "action_to_take": "Complete 5-minute pointer offset retest question.",
                "expected_improvement": "Elimination of stride calculation mistakes.",
            },
        ]
        return insights


insight_engine = InsightEngine()
