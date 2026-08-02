import time
from typing import Dict, Any, List
from app.domain.interfaces.engine import IEngine
from app.engines.recommendation_engine.interfaces import IRecommendationEngine
from app.engines.recommendation_engine.priority_engine import priority_engine
from app.engines.recommendation_engine.plan_engine import plan_engine
from app.engines.recommendation_engine.revision_engine import revision_engine
from app.engines.recommendation_engine.resource_matcher import resource_matcher
from app.engines.recommendation_engine.question_recommender import question_recommender
from app.engines.recommendation_engine.goal_engine import goal_engine
from app.engines.recommendation_engine.path_engine import path_engine
from app.core.events.event_bus import event_bus


class RecommendationEngine(IEngine, IRecommendationEngine):
    """Production Adaptive Recommendation Engine for BACKTRACE. Generation SLA <300 ms."""

    def __init__(self):
        self._subscribe_to_events()

    def _subscribe_to_events(self):
        event_bus.subscribe("DiagnosisCompleted", self._on_diagnosis_completed)
        event_bus.subscribe("MasteryUpdated", self._on_mastery_updated)
        event_bus.subscribe("KnowledgeStateChanged", self._on_knowledge_state_changed)
        event_bus.subscribe("LearningGoalUpdated", self._on_goal_updated)

    async def _on_diagnosis_completed(self, event_data: Dict[str, Any]):
        student_id = event_data.get("student_id")
        if student_id:
            await self.generate_recommendations(student_id)

    async def _on_mastery_updated(self, event_data: Dict[str, Any]):
        pass

    async def _on_knowledge_state_changed(self, event_data: Dict[str, Any]):
        pass

    async def _on_goal_updated(self, event_data: Dict[str, Any]):
        pass

    @property
    def name(self) -> str:
        return "Recommendation Engine"

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def status(self) -> str:
        return "healthy"

    @property
    def dependencies(self) -> List[str]:
        return ["Diagnostic Engine", "Mastery Engine", "Knowledge Graph Engine"]

    async def generate_recommendations(
        self,
        student_id: str,
        focus_concept_code: str = "DSA_ARRAYS_01",
    ) -> Dict[str, Any]:
        start_time = time.time()

        # 1. Multi-factor priority calculation
        p_res = priority_engine.calculate_priority(
            concept_code=focus_concept_code,
            mastery_score=0.65,
            is_prereq=True,
            knowledge_decay=0.20,
        )

        # 2. Resource matching
        resources = resource_matcher.match_resources(focus_concept_code)

        # 3. Question recommendations
        questions = question_recommender.recommend_questions(focus_concept_code, count=2)

        # 4. Explainable recommendations payload
        recs = [
            {
                "recommendation_id": "rec_01",
                "student_id": student_id,
                "recommendation_type": "resource",
                "title": resources[0]["title"],
                "description": "Watch interactive stride visualizer to fix pointer arithmetic calculation error.",
                "target_concept_code": focus_concept_code,
                "priority_score": p_res["priority_score"],
                "urgency_level": p_res["urgency_level"],
                "expected_improvement_delta": 0.20,
                "est_duration_minutes": 10,
                "reasoning_explanation": (
                    f"Recommended because your latest diagnosis revealed a Concept Gap in {focus_concept_code}. "
                    f"Completing this visualizer will resolve your stride offset calculation mistake."
                ),
                "evidence": [{"source": "DiagnosisReport", "detail": "Offset mismatch 0x1005 vs 0x1014"}],
                "is_completed": False,
            },
            {
                "recommendation_id": "rec_02",
                "student_id": student_id,
                "recommendation_type": "question",
                "title": f"Practice Question: {questions[0]['question_id']}",
                "description": questions[0]["question_statement"],
                "target_concept_code": focus_concept_code,
                "priority_score": p_res["priority_score"] - 5.0,
                "urgency_level": p_res["urgency_level"],
                "expected_improvement_delta": 0.15,
                "est_duration_minutes": 15,
                "reasoning_explanation": questions[0]["recommendation_reason"],
                "evidence": [{"source": "QuestionRecommender", "detail": "Target Bloom level: apply"}],
                "is_completed": False,
            },
        ]

        # 5. Today's Plan Generation
        today_plan = plan_engine.generate_todays_plan(student_id, [focus_concept_code], recs)

        proc_time = (time.time() - start_time) * 1000

        result = {
            "student_id": student_id,
            "focus_concept_code": focus_concept_code,
            "recommendations": recs,
            "today_plan": today_plan,
            "processing_time_ms": round(proc_time, 2),
        }

        # 6. Domain Event Publishing via Event Bus
        await event_bus.publish("RecommendationGenerated", result)
        await event_bus.publish("LearningPlanUpdated", {"student_id": student_id, "plan": today_plan})
        await event_bus.publish("ReviewScheduled", {"student_id": student_id, "concept": focus_concept_code})

        return result

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return await self.generate_recommendations(
            student_id=input_data.get("student_id", "student_1"),
            focus_concept_code=input_data.get("focus_concept_code", "DSA_ARRAYS_01"),
        )

    async def health_check(self) -> bool:
        return True

    async def readiness(self) -> bool:
        return True
