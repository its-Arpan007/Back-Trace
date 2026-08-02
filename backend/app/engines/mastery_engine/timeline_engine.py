from datetime import datetime, timezone, timedelta
from typing import Dict, Any, List


class TimelineEngine:
    """Generates concept mastery progression timelines (e.g. Day 1 -> Day 4 -> Day 14)."""

    def generate_timeline(
        self,
        concept_code: str,
        current_mastery: float,
        history: List[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        now = datetime.now(timezone.utc)
        timeline = []

        if history:
            for idx, item in enumerate(history):
                timeline.append({
                    "day_label": f"Day {idx * 3 + 1}",
                    "date": item.get("date", now - timedelta(days=(len(history) - idx) * 3)),
                    "mastery_score": round(item.get("mastery_after", 0.3), 2),
                    "event_summary": item.get("change_reason", "Diagnostic Update"),
                })
        else:
            # Default progression points
            timeline = [
                {"day_label": "Day 1", "date": now - timedelta(days=13), "mastery_score": 0.34, "event_summary": "Initial Diagnostic Attempt"},
                {"day_label": "Day 4", "date": now - timedelta(days=10), "mastery_score": 0.51, "event_summary": "Practice Set 1 Completed"},
                {"day_label": "Day 9", "date": now - timedelta(days=5), "mastery_score": 0.69, "event_summary": "Prerequisite Review Session"},
                {"day_label": "Day 14", "date": now, "mastery_score": round(current_mastery, 2), "event_summary": "Latest Assessment Update"},
            ]

        return timeline


timeline_engine = TimelineEngine()
