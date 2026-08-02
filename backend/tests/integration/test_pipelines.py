import pytest
from app.pipelines.diagnosis_pipeline import diagnosis_pipeline
from app.pipelines.mastery_pipeline import mastery_pipeline
from app.pipelines.recommendation_pipeline import recommendation_pipeline
from app.curriculum.validator import curriculum_validator


@pytest.mark.asyncio
async def test_diagnosis_pipeline_execution():
    report = await diagnosis_pipeline.execute(
        student_id="STD_999",
        question_id="Q_DSA_001",
        given_answer="O(n)",
    )
    assert report["student_id"] == "STD_999"
    assert report["diagnosis_type"] == "MIS_ARRAY_INDEX"
    assert report["engine_version"] == "1.0.0"
    assert report["rule_version"] == "1.0.0"
    assert "decision_outcome" in report
    assert "processing_time_ms" in report


@pytest.mark.asyncio
async def test_mastery_pipeline_execution():
    res = await mastery_pipeline.execute(
        student_id="STD_999",
        concept_id="DSA_ARRAYS_01",
        is_correct=False,
    )
    assert res["student_id"] == "STD_999"
    assert "bayesian_bkt" in res


def test_curriculum_validator_valid_graph():
    graph_data = {
        "graph_version": "1.0.0",
        "domain": "dsa",
        "nodes": ["C1", "C2"],
        "edges": [{"source": "C1", "target": "C2"}],
    }
    concepts = [{"id": "C1"}, {"id": "C2"}]
    res = curriculum_validator.validate_graph(graph_data, concepts)
    assert res["valid"] is True
    assert len(res["errors"]) == 0
