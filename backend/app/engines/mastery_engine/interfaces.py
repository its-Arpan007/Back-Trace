from abc import ABC, abstractmethod
from typing import Dict, Any


class IMasteryEngine(ABC):
    @abstractmethod
    async def calculate_mastery(self, student_id: str, concept_id: str) -> float:
        pass
