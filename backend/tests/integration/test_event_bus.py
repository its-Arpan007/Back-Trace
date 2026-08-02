import pytest
from app.core.events.event_bus import EventBus
from app.core.events.events import QuestionSubmittedEvent


@pytest.mark.asyncio
async def test_event_bus_publish_subscribe():
    bus = EventBus()
    received_events = []

    async def sample_handler(event: QuestionSubmittedEvent):
        received_events.append(event)

    bus.subscribe(QuestionSubmittedEvent, sample_handler)

    test_event = QuestionSubmittedEvent(student_id="S100", question_id="Q200", given_answer="A")
    await bus.publish(test_event)

    assert len(received_events) == 1
    assert received_events[0].student_id == "S100"
