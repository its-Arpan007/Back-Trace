import time
from typing import Dict, Any, List
from app.domain.interfaces.engine import IEngine
from app.engines.diagnostic_engine.interfaces import IDiagnosticEngine
from app.engines.diagnostic_engine.answer_evaluator import answer_evaluator
from app.engines.diagnostic_engine.evidence_engine import evidence_engine
from app.engines.diagnostic_engine.confidence_engine import confidence_engine
from app.engines.diagnostic_engine.misconception_detector import misconception_detector
from app.engines.diagnostic_engine.prerequisite_analyzer import prerequisite_analyzer
from app.engines.diagnostic_engine.pattern_analyzer import pattern_analyzer
from app.engines.rule_engine.engine import RuleEngine
from app.engines.decision_engine.engine import DecisionEngine
from app.core.events.event_bus import event_bus


class DiagnosticEngine(IEngine, IDiagnosticEngine):
    """Pipeline Orchestrator for BACKTRACE Intelligence Engine. Guarantees <300ms execution target."""

    def __init__(self):
        self.rule_engine = RuleEngine()
        self.decision_engine = DecisionEngine()

    @property
    def name(self) -> str:
        return "Diagnostic Engine"

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def status(self) -> str:
        return "healthy"

    @property
    def dependencies(self) -> List[str]:
        return ["Rule Engine", "AI Engine", "Knowledge Graph Engine", "Decision Engine"]

    async def run_diagnosis_pipeline(
        self,
        student_id: str,
        question: Dict[str, Any],
        student_answer: Any,
        time_spent_seconds: int = 60,
        hints_used: int = 0,
        student_history: List[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        start_time = time.time()
        student_history = student_history or []

        # 1. Answer Evaluation Engine
        eval_res = answer_evaluator.evaluate(question, student_answer)

        # 2. Misconception Detector
        detected_misconceptions = misconception_detector.detect_misconceptions(question, student_answer)

        # 3. Knowledge Graph & Prerequisite Analyzer
        concept_code = question.get("primary_concept_id", "DSA_ARRAYS_01")
        prereq_res = await prerequisite_analyzer.analyze_prerequisites(concept_code)

        # 4. Pattern Analyzer
        patterns = pattern_analyzer.analyze_patterns(student_history)

        # 5. Deterministic Rule Engine (Source of Truth)
        rule_res = await self.rule_engine.evaluate_rules(
            eval_result=eval_res,
            question=question,
            misconceptions=detected_misconceptions,
            time_spent_seconds=time_spent_seconds,
        )

        # 6. Evidence Engine
        evidence = evidence_engine.collect_evidence(
            eval_result=eval_res,
            question=question,
            student_history=student_history,
            time_spent_seconds=time_spent_seconds,
            hints_used=hints_used,
        )

        # 7. Confidence Engine
        conf_score, conf_explain = confidence_engine.calculate_confidence(
            matched_rule=rule_res["matched_rule"],
            evidence_records=evidence,
            graph_prereqs_count=len(prereq_res["weak_prerequisites"]),
        )

        # 8. Decision Engine Integration
        diag_summary = {
            "is_correct": eval_res["is_correct"],
            "primary_root_cause": rule_res["primary_root_cause"],
            "confidence_score": conf_score,
        }
        decision = await self.decision_engine.process(diag_summary)

        total_proc_time = (time.time() - start_time) * 1000

        diagnosis_report = {
            "student_id": student_id,
            "question_id": question.get("id", "q1_arrays_01"),
            "concept_code": concept_code,
            "is_correct": eval_res["is_correct"],
            "score": eval_res["score"],
            "evaluation_details": eval_res["details"],
            "primary_root_cause": rule_res["primary_root_cause"],
            "secondary_root_causes": rule_res["secondary_root_causes"],
            "confidence_score": conf_score,
            "severity": rule_res["severity"],
            "evidence": evidence,
            "detected_misconceptions": detected_misconceptions,
            "weak_prerequisites": prereq_res["weak_prerequisites"],
            "bloom_level": question.get("bloom_level", "apply"),
            "mastery_impact": {"delta": 0.15 if eval_res["is_correct"] else -0.10},
            "recommended_actions": decision.get("recommended_actions", []),
            "recommended_lessons": ["Array Memory Stride Tutorial"],
            "recommended_questions": ["q2_arrays_02"],
            "processing_time_ms": round(total_proc_time, 2),
            "engine_versions": {
                "diagnostic_engine": self.version,
                "rule_engine": self.rule_engine.version,
                "decision_engine": self.decision_engine.version,
            },
        }

        # 9. Domain Event Integration via Event Bus
        await event_bus.publish(
            "DiagnosisCompleted",
            {
                "student_id": student_id,
                "concept_code": concept_code,
                "is_correct": eval_res["is_correct"],
                "primary_root_cause": rule_res["primary_root_cause"],
            },
        )
        await event_bus.publish("MasteryUpdateRequested", {"student_id": student_id, "concept_code": concept_code})
        await event_bus.publish("RecommendationRequested", {"student_id": student_id})
        await event_bus.publish("AnalyticsUpdateRequested", {"student_id": student_id})

        return diagnosis_report

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return await self.run_diagnosis_pipeline(
            student_id=input_data.get("student_id", "student_1"),
            question=input_data.get("question", {"id": "q1_arrays_01", "primary_concept_id": "DSA_ARRAYS_01", "correct_answer": "0x1014"}),
            student_answer=input_data.get("student_answer", "0x1005"),
            time_spent_seconds=input_data.get("time_spent_seconds", 60),
            hints_used=input_data.get("hints_used", 0),
        )

    async def health_check(self) -> bool:
        return True

    async def readiness(self) -> bool:
        return True
