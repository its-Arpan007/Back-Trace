import asyncio
import logging
from typing import Callable, Coroutine, Dict, List, Type, Any
from app.core.events.base_event import BaseEvent

logger = logging.getLogger("backtrace.event_bus")

EventHandler = Callable[[Any], Coroutine[Any, Any, None]]


class EventBus:
    def __init__(self) -> None:
        self._handlers: Dict[Type[BaseEvent], List[EventHandler]] = {}

    def subscribe(self, event_type: Type[BaseEvent], handler: EventHandler) -> None:
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)
        logger.info(f"Subscribed handler '{handler.__name__}' to event '{event_type.__name__}'")

    async def publish(self, event: BaseEvent) -> None:
        event_type = type(event)
        handlers = self._handlers.get(event_type, [])
        logger.info(f"Publishing event '{event.event_type}' (id: {event.event_id}) to {len(handlers)} handlers")

        for handler in handlers:
            try:
                await handler(event)
            except Exception as e:
                logger.error(f"Error in event handler '{handler.__name__}' for event '{event.event_type}': {e}", exc_info=True)


event_bus = EventBus()
