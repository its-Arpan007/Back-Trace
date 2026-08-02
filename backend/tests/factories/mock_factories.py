from app.domain.entities.student import StudentEntity
from app.domain.entities.question import QuestionEntity
from app.domain.entities.diagnosis import DiagnosisEntity


class MockFactory:
    @staticmethod
    def create_student(student_id: str = "STD_001") -> StudentEntity:
        return StudentEntity(
            id=student_id,
            email="teststudent@backtrace.ai",
            full_name="Test Student",
            role="student",
        )

    @staticmethod
    def create_question(question_id: str = "Q_001") -> QuestionEntity:
        return QuestionEntity(
            id=question_id,
            concept_id="DSA_ARRAYS_01",
            prompt="Sample Question",
            question_type="multiple_choice",
            difficulty="medium",
        )
