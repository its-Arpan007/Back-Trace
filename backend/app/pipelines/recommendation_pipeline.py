from typing import Dict, Any
from app.engines.engine_registry import engine_registry


class RecommendationPipeline:
    async def execute(self, student_id: str) -> Dict[str, Any]:
        rec_engine = engine_registry.get("recommendation")
        decision_engine = engine_registry.get("decision")

        recs = await rec_engine.process({"student_id": student_id})
        decision = await decision_engine.process({"is_correct": False, "difficulty": "medium"})

        return {
            "student_id": student_id,
            "recommendations": recs["recommendations"],
            "decision_context": decision,
        }


recommendation_pipeline = RecommendationPipeline()
