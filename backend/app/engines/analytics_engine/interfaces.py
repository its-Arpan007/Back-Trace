from abc import ABC, abstractmethod
from typing import Dict, Any


class IAnalyticsEngine(ABC):
    @abstractmethod
    async def compute_student_analytics(self, student_id: str) -> Dict[str, Any]:
        pass
