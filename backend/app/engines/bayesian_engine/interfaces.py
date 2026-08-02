from abc import ABC, abstractmethod
from typing import Dict, Any


class IBayesianEngine(ABC):
    @abstractmethod
    async def update_bkt_state(self, student_id: str, concept_id: str, is_correct: bool) -> Dict[str, Any]:
        pass
