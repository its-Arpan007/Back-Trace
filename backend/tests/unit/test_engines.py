import pytest
from app.engines.diagnostic_engine.engine import DiagnosticEngine
from app.engines.knowledge_graph_engine.engine import KnowledgeGraphEngine
from app.engines.mastery_engine.engine import MasteryEngine


@pytest.mark.asyncio
async def test_diagnostic_engine_process():
    engine = DiagnosticEngine()
    result = await engine.process({"student_id": "S1", "question_id": "Q1", "answer": "B"})
    assert result["diagnosis_type"] == "misconception"
    assert "diagnosis_id" in result


@pytest.mark.asyncio
async def test_knowledge_graph_engine_prereqs():
    engine = KnowledgeGraphEngine()
    prereqs = await engine.get_concept_prerequisites("C101")
    assert len(prereqs) == 2


@pytest.mark.asyncio
async def test_mastery_engine_calculation():
    engine = MasteryEngine()
    score = await engine.calculate_mastery("S1", "C101")
    assert score == 0.85
