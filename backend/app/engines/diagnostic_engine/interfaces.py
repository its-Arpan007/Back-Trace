from abc import ABC, abstractmethod
from typing import Dict, Any


class IDiagnosticEngine(ABC):
    @abstractmethod
    async def diagnose_error(self, student_id: str, question_id: str, answer: str) -> Dict[str, Any]:
        pass
