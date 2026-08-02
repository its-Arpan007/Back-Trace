from abc import ABC, abstractmethod
from typing import Dict, Any, List


class IRuleEngine(ABC):
    @abstractmethod
    async def evaluate_rules(self, student_id: str, question_id: str, answer: str) -> Dict[str, Any]:
        pass
