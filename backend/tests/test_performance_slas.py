import pytest
import time
from app.engines.diagnostic_engine.engine import DiagnosticEngine
from app.engines.mastery_engine.engine import MasteryEngine
from app.engines.recommendation_engine.engine import RecommendationEngine
from app.engines.analytics_engine.engine import AnalyticsEngine
from app.engines.ai_engine.context_builder import context_builder


@pytest.mark.asyncio
async def test_diagnosis_engine_sla():
    engine = DiagnosticEngine()
    start = time.time()
    res = await engine.run_pipeline("11111111-1111-1111-1111-111111111111", "q1_arrays_01", "0x1005", 45)
    elapsed_ms = (time.time() - start) * 1000
    assert elapsed_ms < 300.0 # Strict <300ms SLA
    assert res["pipeline_time_ms"] < 300.0


@pytest.mark.asyncio
async def test_mastery_engine_sla():
    engine = MasteryEngine()
    start = time.time()
    res = await engine.process_learning_event("11111111-1111-1111-1111-111111111111", "DSA_ARRAYS_01", False)
    elapsed_ms = (time.time() - start) * 1000
    assert elapsed_ms < 100.0 # Strict <100ms SLA
    assert res["processing_time_ms"] < 100.0


@pytest.mark.asyncio
async def test_recommendation_engine_sla():
    engine = RecommendationEngine()
    start = time.time()
    res = await engine.generate_recommendations("11111111-1111-1111-1111-111111111111", focus_concept_code="DSA_ARRAYS_01")
    elapsed_ms = (time.time() - start) * 1000
    assert elapsed_ms < 300.0 # Strict <300ms SLA
    assert res["processing_time_ms"] < 300.0


@pytest.mark.asyncio
async def test_analytics_engine_sla():
    engine = AnalyticsEngine()
    start = time.time()
    res = await engine.generate_student_analytics("11111111-1111-1111-1111-111111111111")
    elapsed_ms = (time.time() - start) * 1000
    assert elapsed_ms < 500.0 # Strict <500ms SLA
    assert res["processing_time_ms"] < 500.0


def test_ai_context_builder_sla():
    start = time.time()
    ctx = context_builder.build_context("11111111-1111-1111-1111-111111111111", "DSA_ARRAYS_01")
    elapsed_ms = (time.time() - start) * 1000
    assert elapsed_ms < 100.0 # Strict <100ms SLA
    assert ctx["context_build_time_ms"] < 100.0
