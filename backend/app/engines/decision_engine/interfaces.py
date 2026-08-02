from abc import ABC, abstractmethod
from typing import Dict, Any


class IDecisionEngine(ABC):
    @abstractmethod
    async def make_decision(self, diagnosis_result: Dict[str, Any]) -> Dict[str, Any]:
        pass
