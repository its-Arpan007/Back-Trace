from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseLLMProvider(ABC):
    @abstractmethod
    async def generate_response(self, prompt: str, context: Dict[str, Any]) -> str:
        pass

    @property
    @abstractmethod
    def provider_name(self) -> str:
        pass
