import pytest
from app.engines.recommendation_engine.engine import RecommendationEngine
from app.engines.recommendation_engine.priority_engine import priority_engine
from app.engines.recommendation_engine.plan_engine import plan_engine
from app.engines.recommendation_engine.revision_engine import revision_engine
from app.engines.recommendation_engine.resource_matcher import resource_matcher
from app.engines.recommendation_engine.path_engine import path_engine


@pytest.mark.asyncio
async def test_priority_engine():
    res = priority_engine.calculate_priority("DSA_ARRAYS_01", mastery_score=0.40, is_prereq=True, knowledge_decay=0.30)
    assert res["priority_score"] >= 80.0
    assert res["urgency_level"] == "critical"


@pytest.mark.asyncio
async def test_recommendation_engine_performance_sla():
    engine = RecommendationEngine()
    res = await engine.generate_recommendations("11111111-1111-1111-1111-111111111111", focus_concept_code="DSA_ARRAYS_01")
    assert len(res["recommendations"]) >= 2
    assert res["processing_time_ms"] < 300.0 # Strict <300ms SLA


def test_learning_plan_engine_sla():
    plan = plan_engine.generate_todays_plan("11111111-1111-1111-1111-111111111111", ["DSA_ARRAYS_01"], [])
    assert len(plan["tasks"]) == 3
    assert plan["processing_time_ms"] < 500.0 # Strict <500ms SLA


def test_adaptive_path_engine():
    path = path_engine.generate_path("DSA_ARRAYS_01")
    assert len(path["nodes"]) == 4
    assert path["nodes"][0]["name"] == "Comparison Operators"
