from abc import ABC, abstractmethod
from typing import Any, Callable, Coroutine


class IEventBus(ABC):
    """Abstract interface for Async Domain Event Bus."""

    @abstractmethod
    async def publish(self, event: Any) -> None:
        pass

    @abstractmethod
    def subscribe(self, event_type: type, handler: Callable[[Any], Coroutine[Any, Any, None]]) -> None:
        pass
