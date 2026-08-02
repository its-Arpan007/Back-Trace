from abc import ABC, abstractmethod
from typing import List, Dict, Any


class IRecommendationEngine(ABC):
    @abstractmethod
    async def generate_recommendations(self, student_id: str) -> List[Dict[str, Any]]:
        pass
