from abc import ABC, abstractmethod
from typing import Dict, Any


class IAIEngine(ABC):
    @abstractmethod
    async def generate_explanation(self, root_cause: str, concept: str) -> Dict[str, Any]:
        pass
