import math
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, Tuple


class KnowledgeDecayEngine:
    """Calculates Ebbinghaus Knowledge Decay curve R = e^(-t / S) and schedules review dates."""

    def calculate_decay(
        self,
        last_practiced: datetime,
        retention_half_life_days: float = 14.0,
    ) -> Tuple[float, float, datetime]:
        now = datetime.now(timezone.utc)
        if not last_practiced:
            days_elapsed = 0.0
        else:
            days_elapsed = max((now - last_practiced).total_seconds() / 86400.0, 0.0)

        # Strength parameter S derived from half life
        S = retention_half_life_days / math.log(2.0)
        retention = math.exp(-days_elapsed / max(S, 1e-5))
        knowledge_decay = 1.0 - retention

        # Schedule review when retention drops below 0.75
        days_until_review = max(S * math.log(1.0 / 0.75), 1.0)
        review_date = now + timedelta(days=days_until_review)

        return round(retention, 4), round(knowledge_decay, 4), review_date


decay_engine = KnowledgeDecayEngine()
