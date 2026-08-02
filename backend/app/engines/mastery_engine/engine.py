import time
from datetime import datetime, timezone
from typing import Dict, Any, List
from app.domain.interfaces.engine import IEngine
from app.engines.mastery_engine.interfaces import IMasteryEngine
from app.engines.bayesian_engine.engine import BayesianEngine
from app.engines.mastery_engine.decay_engine import decay_engine
from app.engines.mastery_engine.velocity_engine import velocity_engine
from app.engines.mastery_engine.prediction_engine import prediction_engine
from app.core.events.event_bus import event_bus


class MasteryEngine(IEngine, IMasteryEngine):
    """Production Mastery Engine for BACKTRACE. Incremental update SLA <100 ms."""

    def __init__(self):
        self.bayesian_engine = BayesianEngine()
        self._subscribe_to_events()

    def _subscribe_to_events(self):
        # Register Event Bus listeners for non-blocking asynchronous updates
        event_bus.subscribe("DiagnosisCompleted", self._on_diagnosis_completed)
        event_bus.subscribe("LearningSessionCompleted", self._on_session_completed)

    async def _on_diagnosis_completed(self, event_data: Dict[str, Any]):
        student_id = event_data.get("student_id")
        concept_code = event_data.get("concept_code")
        is_correct = event_data.get("is_correct", False)
        if student_id and concept_code:
            await self.update_concept_mastery(student_id, concept_code, is_correct)

    async def _on_session_completed(self, event_data: Dict[str, Any]):
        pass

    @property
    def name(self) -> str:
        return "Mastery Engine"

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def status(self) -> str:
        return "healthy"

    @property
    def dependencies(self) -> List[str]:
        return ["Bayesian Engine"]

    async def update_concept_mastery(
        self,
        student_id: str,
        concept_code: str,
        is_correct: bool,
        current_p_know: float = 0.20,
        last_practiced: datetime = None,
    ) -> Dict[str, Any]:
        start_time = time.time()

        # 1. Bayesian Knowledge Tracing (BKT) Update
        post, p_next = await self.bayesian_engine.calculate_posterior(
            p_know=current_p_know,
            is_correct=is_correct,
        )

        # 2. Knowledge Decay Calculation
        retention, decay, review_date = decay_engine.calculate_decay(
            last_practiced=last_practiced or datetime.now(timezone.utc),
        )

        # 3. Incremental Mastery Score & Trend
        mastery_score = round(p_next * retention, 4)
        trend = "improving" if is_correct else ("regressing" if current_p_know > 0.40 else "plateau")

        proc_time = (time.time() - start_time) * 1000

        result = {
            "student_id": student_id,
            "concept_code": concept_code,
            "is_correct": is_correct,
            "previous_mastery": current_p_know,
            "current_mastery": mastery_score,
            "p_know_next": p_next,
            "retention_score": retention,
            "knowledge_decay": decay,
            "next_recommended_review": review_date,
            "mastery_trend": trend,
            "processing_time_ms": round(proc_time, 2),
        }

        # 4. Domain Event Publishing via Event Bus
        await event_bus.publish("MasteryUpdated", result)
        await event_bus.publish("KnowledgeStateChanged", {"student_id": student_id, "concept_code": concept_code, "mastery": mastery_score})
        await event_bus.publish("StudentModelUpdated", {"student_id": student_id})
        if decay > 0.25:
            await event_bus.publish("ReviewRequired", {"student_id": student_id, "concept_code": concept_code})

        return result

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return await self.update_concept_mastery(
            student_id=input_data.get("student_id", "student_1"),
            concept_code=input_data.get("concept_code", "DSA_ARRAYS_01"),
            is_correct=input_data.get("is_correct", True),
            current_p_know=input_data.get("current_p_know", 0.20),
        )

    async def health_check(self) -> bool:
        return True

    async def readiness(self) -> bool:
        return True
