import pytest
from app.engines.diagnostic_engine.engine import DiagnosticEngine
from app.engines.diagnostic_engine.answer_evaluator import answer_evaluator
from app.engines.diagnostic_engine.evidence_engine import evidence_engine
from app.engines.diagnostic_engine.confidence_engine import confidence_engine
from app.engines.diagnostic_engine.misconception_detector import misconception_detector
from app.engines.rule_engine.engine import RuleEngine


@pytest.mark.asyncio
async def test_answer_evaluator():
    q = {"question_type": "MCQ", "correct_answer": "0x1014", "max_score": 10.0}
    res_correct = answer_evaluator.evaluate(q, "0x1014")
    assert res_correct["is_correct"] is True
    assert res_correct["score"] == 10.0

    res_incorrect = answer_evaluator.evaluate(q, "0x1005")
    assert res_incorrect["is_correct"] is False
    assert res_incorrect["score"] == 0.0


@pytest.mark.asyncio
async def test_diagnostic_pipeline_performance():
    engine = DiagnosticEngine()
    q = {
        "id": "q1_arrays_01",
        "primary_concept_id": "DSA_ARRAYS_01",
        "correct_answer": "0x1014",
        "bloom_level": "apply",
        "estimated_time_seconds": 120,
    }

    report = await engine.run_diagnosis_pipeline(
        student_id="11111111-1111-1111-1111-111111111111",
        question=q,
        student_answer="0x1005",
        time_spent_seconds=45,
        hints_used=1,
    )

    assert report["is_correct"] is False
    assert "primary_root_cause" in report
    assert report["confidence_score"] > 0.0
    assert report["processing_time_ms"] < 300.0 # Strict <300ms execution target


def test_confidence_engine():
    score, explain = confidence_engine.calculate_confidence(
        matched_rule={"confidence_weight": 0.85},
        evidence_records=[{"source": "time", "weight": 0.75}],
        graph_prereqs_count=2,
    )
    assert score >= 85.0
    assert "Confidence" in explain
