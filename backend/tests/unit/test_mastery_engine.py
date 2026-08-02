import pytest
from datetime import datetime, timezone
from app.engines.bayesian_engine.engine import BayesianEngine
from app.engines.mastery_engine.engine import MasteryEngine
from app.engines.mastery_engine.decay_engine import decay_engine
from app.engines.mastery_engine.prediction_engine import prediction_engine
from app.engines.mastery_engine.timeline_engine import timeline_engine


@pytest.mark.asyncio
async def test_bayesian_knowledge_tracing():
    bkt = BayesianEngine()
    post, p_next = await bkt.calculate_posterior(p_know=0.20, is_correct=True)
    assert post > 0.20
    assert p_next > post


@pytest.mark.asyncio
async def test_mastery_engine_incremental_update_performance():
    engine = MasteryEngine()
    result = await engine.update_concept_mastery(
        student_id="11111111-1111-1111-1111-111111111111",
        concept_code="DSA_ARRAYS_01",
        is_correct=True,
        current_p_know=0.50,
    )

    assert result["current_mastery"] > 0.50
    assert result["processing_time_ms"] < 100.0 # Strict <100ms update SLA


def test_knowledge_decay_engine():
    now = datetime.now(timezone.utc)
    retention, decay, review_date = decay_engine.calculate_decay(last_practiced=now, retention_half_life_days=14.0)
    assert retention > 0.95
    assert decay < 0.05


def test_prediction_engine_performance():
    pred = prediction_engine.predict_mastery(current_mastery=0.75, p_know=0.80, trend="improving", attempts_count=5)
    assert pred["predicted_mastery"] > 0.75
    assert pred["readiness_score"] >= 0.80
