from abc import ABC, abstractmethod
from typing import Any, Dict


class IEngine(ABC):
    """Abstract interface contract for all BACKTRACE Learning Intelligence Engines."""

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        pass
