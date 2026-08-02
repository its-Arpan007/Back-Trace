import pytest
from app.engines.question_engine.engine import QuestionEngine
from app.engines.question_engine.validator import question_validator
from app.engines.question_engine.exporter import question_exporter
from app.engines.question_engine.importer import question_importer


@pytest.mark.asyncio
async def test_question_engine_adaptive_selection():
    engine = QuestionEngine()
    questions = await engine.select_adaptive_questions("student_1", ["DSA_ARRAYS_01"], count=3)
    assert len(questions) == 3


@pytest.mark.asyncio
async def test_question_engine_practice_set_generation():
    engine = QuestionEngine()
    pset = await engine.generate_practice_set(["DSA_ARRAYS_01"], "medium", count=2)
    assert pset["total_questions"] == 2
    assert "practice_set_id" in pset


def test_question_validator():
    q_data = [
        {
            "id": "q1",
            "slug": "test-q1",
            "question_statement": "Sample question",
            "question_type": "MCQ",
            "bloom_level": "apply",
        }
    ]
    report = question_validator.validate_questions(q_data)
    assert report["valid"] is True
    assert report["total_questions"] == 1


def test_question_exporter():
    q_data = [{"id": "q1", "title": "Sample Title", "slug": "sample-title"}]
    json_out = question_exporter.export_to_json(q_data)
    assert "sample-title" in json_out
