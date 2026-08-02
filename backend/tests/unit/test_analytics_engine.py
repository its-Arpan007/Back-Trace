import pytest
from app.engines.analytics_engine.engine import AnalyticsEngine
from app.engines.analytics_engine.aggregation_engine import aggregation_engine
from app.engines.analytics_engine.insight_engine import insight_engine
from app.engines.analytics_engine.intervention_engine import intervention_engine
from app.engines.analytics_engine.predictive_engine import predictive_engine
from app.engines.analytics_engine.report_engine import report_engine


@pytest.mark.asyncio
async def test_aggregation_engine_sla():
    res = aggregation_engine.aggregate_student_metrics("11111111-1111-1111-1111-111111111111", [{"current_mastery": 0.88}], [])
    assert res["overall_mastery_avg"] == 0.88
    assert res["processing_time_ms"] < 100.0 # Strict <100ms SLA


@pytest.mark.asyncio
async def test_analytics_engine_performance_sla():
    engine = AnalyticsEngine()
    res = await engine.generate_student_analytics("11111111-1111-1111-1111-111111111111")
    assert "metrics" in res
    assert len(res["insights"]) >= 2
    assert res["processing_time_ms"] < 500.0 # Strict <500ms SLA


def test_predictive_engine_sla():
    preds = predictive_engine.generate_predictions("11111111-1111-1111-1111-111111111111", 0.78)
    assert preds["exam_readiness"] >= 0.80
    assert preds["processing_time_ms"] < 300.0 # Strict <300ms SLA


def test_insight_engine():
    insights = insight_engine.generate_student_insights("11111111-1111-1111-1111-111111111111", 0.78, ["DSA_ARRAYS_01"])
    assert len(insights) >= 2
    assert "natural_language_statement" in insights[0]
