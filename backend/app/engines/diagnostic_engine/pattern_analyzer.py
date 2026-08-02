from typing import List, Dict, Any


class PatternAnalyzer:
    """Analyzes student attempt history to detect recurring mistake patterns (guessing, reading errors, time pressure)."""

    def analyze_patterns(self, student_history: List[Dict[str, Any]]) -> List[str]:
        patterns: List[str] = []
        if not student_history:
            return patterns

        fast_fails = sum(1 for h in student_history if not h.get("is_correct") and h.get("time_spent_seconds", 60) < 20)
        if fast_fails >= 2:
            patterns.append("Repeated Guessing / Rushing")

        hint_heavy_fails = sum(1 for h in student_history if not h.get("is_correct") and h.get("hints_used", 0) >= 2)
        if hint_heavy_fails >= 2:
            patterns.append("Repeated Prerequisite Struggle")

        return patterns


pattern_analyzer = PatternAnalyzer()
