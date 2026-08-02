import pytest
from app.domain.entities.student import StudentEntity
from app.domain.value_objects.score import ScoreValueObject
from app.domain.value_objects.difficulty import DifficultyValueObject


def test_student_entity_deactivation():
    student = StudentEntity(id="1", email="student@test.com")
    assert student.is_active is True
    student.deactivate()
    assert student.is_active is False


def test_score_value_object():
    score = ScoreValueObject(0.85)
    assert score.percentage == 85.0

    with pytest.raises(ValueError):
        ScoreValueObject(1.5)


def test_difficulty_value_object():
    diff = DifficultyValueObject("HARD")
    assert diff.level == "hard"

    with pytest.raises(ValueError):
        DifficultyValueObject("impossible")
