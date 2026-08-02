from abc import ABC, abstractmethod
from typing import Dict, Any, List


class IKnowledgeGraphEngine(ABC):
    @abstractmethod
    async def get_concept_prerequisites(self, concept_id: str) -> List[str]:
        pass
