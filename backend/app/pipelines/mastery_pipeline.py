from typing import Dict, Any
from app.engines.engine_registry import engine_registry


class MasteryPipeline:
    async def execute(self, student_id: str, concept_id: str, is_correct: bool) -> Dict[str, Any]:
        bayesian_engine = engine_registry.get("bayesian")
        mastery_engine = engine_registry.get("mastery")

        bkt_res = await bayesian_engine.process({
            "student_id": student_id,
            "concept_id": concept_id,
            "is_correct": is_correct,
        })
        mastery_res = await mastery_engine.process({
            "student_id": student_id,
            "concept_id": concept_id,
        })

        return {
            "student_id": student_id,
            "concept_id": concept_id,
            "bayesian_bkt": bkt_res,
            "mastery_level": mastery_res["level"],
        }


mastery_pipeline = MasteryPipeline()
