import time
import logging
from typing import Dict, Any
from app.engines.engine_registry import engine_registry

logger = logging.getLogger("backtrace.pipeline.diagnosis")


class DiagnosisPipeline:
    """Orchestrates end-to-end diagnostic workflow through independent engine pipeline."""

    async def execute(self, student_id: str, question_id: str, given_answer: str) -> Dict[str, Any]:
        start_time = time.time()
        logger.info(f"Executing Diagnosis Pipeline for student '{student_id}', question '{question_id}'")

        # 1. Rule Engine Evaluation
        rule_engine = engine_registry.get("rule")
        rule_res = await rule_engine.process({"student_id": student_id, "question_id": question_id, "answer": given_answer})

        # 2. Knowledge Graph Traversal
        kg_engine = engine_registry.get("knowledge_graph")
        kg_res = await kg_engine.process({"concept_id": "DSA_ARRAYS_01"})

        # 3. Mastery Engine Calculation
        mastery_engine = engine_registry.get("mastery")
        mastery_res = await mastery_engine.process({"student_id": student_id, "concept_id": "DSA_ARRAYS_01"})

        # 4. Recommendation Engine Generation
        rec_engine = engine_registry.get("recommendation")
        rec_res = await rec_engine.process({"student_id": student_id})

        # 5. Analytics Engine Logging
        analytics_engine = engine_registry.get("analytics")
        analytics_res = await analytics_engine.process({"student_id": student_id})

        # 6. Diagnostic Engine Final Report Assembly
        diag_engine = engine_registry.get("diagnostic")
        diag_report = await diag_engine.process({"student_id": student_id, "question_id": question_id, "answer": given_answer})

        # 7. Decision Engine Action Determination
        decision_engine = engine_registry.get("decision")
        decision_res = await decision_engine.process({"is_correct": False, "difficulty": "medium"})

        processing_time = round((time.time() - start_time) * 1000, 2)
        diag_report["processing_time_ms"] = processing_time
        diag_report["decision_outcome"] = decision_res
        diag_report["mastery_state"] = mastery_res
        diag_report["recommendations"] = rec_res["recommendations"]

        return diag_report


diagnosis_pipeline = DiagnosisPipeline()
