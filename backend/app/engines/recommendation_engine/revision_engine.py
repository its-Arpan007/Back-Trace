from datetime import datetime, timezone, timedelta
from typing import Dict, Any, List


class RevisionEngine:
    """Schedules spaced revision sessions and decay recovery queues."""

    def schedule_revisions(
        self,
        student_id: str,
        decay_records: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        now = datetime.now(timezone.utc)
        revisions = []

        for record in decay_records:
            concept = record.get("concept_code", "DSA_ARRAYS_01")
            decay = record.get("knowledge_decay", 0.20)
            
            revisions.append({
                "student_id": student_id,
                "concept_code": concept,
                "scheduled_date": now + timedelta(days=2),
                "revision_reason": f"Knowledge Decay ({decay*100:.0f}%) reached threshold.",
                "urgency": "high" if decay > 0.30 else "medium",
            })

        if not revisions:
            revisions.append({
                "student_id": student_id,
                "concept_code": "DSA_TREES_01",
                "scheduled_date": now + timedelta(days=1),
                "revision_reason": "Spaced Revision Interval Reached",
                "urgency": "medium",
            })

        return revisions


revision_engine = RevisionEngine()
