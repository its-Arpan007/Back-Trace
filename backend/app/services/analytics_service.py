import uuid
from typing import Optional, List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.analytics import StudentAnalyticsModel
from app.repositories.analytics_repository import AnalyticsRepository
from app.engines.analytics_engine.engine import AnalyticsEngine
from app.engines.analytics_engine.predictive_engine import predictive_engine
from app.engines.analytics_engine.report_engine import report_engine
from app.schemas.analytics import (
    StudentAnalyticsDTO,
    TeacherAnalyticsDTO,
    InstitutionAnalyticsDTO,
    ConceptAnalyticsDTO,
    QuestionAnalyticsDTO,
    RecommendationAnalyticsDTO,
    PredictionAnalyticsDTO,
    PerformanceReportDTO,
)


class AnalyticsService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = AnalyticsRepository(db)
        self.engine = AnalyticsEngine()

    async def get_student_analytics(self, student_id: uuid.UUID) -> StudentAnalyticsDTO:
        sa = await self.repo.get_student_analytics(student_id)
        if not sa:
            sa = await self.repo.upsert_student_analytics(student_id, {
                "learning_progress_pct": 78.5,
                "overall_mastery_avg": 0.78,
                "confidence_trend_score": 0.88,
                "retention_trend_score": 0.92,
                "learning_velocity": 1.45,
                "time_spent_total_minutes": 240,
                "practice_consistency_score": 0.95,
                "weak_concepts_json": ["DSA_ARRAYS_01"],
                "strong_concepts_json": ["DSA_COMPARISONS_01"],
                "recommendation_acceptance_rate": 0.88,
                "goal_progress_pct": 75.0,
                "exam_readiness_score": 0.82,
            })

        return StudentAnalyticsDTO(
            student_id=str(sa.student_id),
            learning_progress_pct=sa.learning_progress_pct,
            overall_mastery_avg=sa.overall_mastery_avg,
            confidence_trend_score=sa.confidence_trend_score,
            retention_trend_score=sa.retention_trend_score,
            learning_velocity=sa.learning_velocity,
            time_spent_total_minutes=sa.time_spent_total_minutes,
            practice_consistency_score=sa.practice_consistency_score,
            weak_concepts=sa.weak_concepts_json or [],
            strong_concepts=sa.strong_concepts_json or [],
            recommendation_acceptance_rate=sa.recommendation_acceptance_rate,
            goal_progress_pct=sa.goal_progress_pct,
            exam_readiness_score=sa.exam_readiness_score,
        )

    async def get_teacher_analytics(self, teacher_id: uuid.UUID) -> TeacherAnalyticsDTO:
        return TeacherAnalyticsDTO(
            teacher_id=str(teacher_id),
            class_performance_avg=0.78,
            top_misconceptions=[
                {"misconception_code": "MIS_OFFSET_01", "frequency": 14, "name": "Array Stride Multiplication Mismatch"},
            ],
            weak_concepts_summary=[
                {"concept_code": "DSA_ARRAYS_01", "weak_student_count": 5},
            ],
            intervention_candidates_count=2,
            recommendation_success_rate=0.88,
        )

    async def get_institution_analytics(self, institution_id: uuid.UUID) -> InstitutionAnalyticsDTO:
        return InstitutionAnalyticsDTO(
            institution_id=str(institution_id),
            total_active_students=150,
            course_completion_rate=0.82,
            teacher_performance_score=0.90,
            daily_active_users=120,
            platform_retention_rate=0.94,
            system_health_pct=99.9,
        )

    async def get_concept_analytics(self) -> List[ConceptAnalyticsDTO]:
        return [
            ConceptAnalyticsDTO(concept_code="DSA_ARRAYS_01", avg_mastery=0.75, avg_confidence=0.80, failure_rate=0.18, improvement_rate=0.15),
            ConceptAnalyticsDTO(concept_code="DSA_TREES_01", avg_mastery=0.65, avg_confidence=0.70, failure_rate=0.25, improvement_rate=0.10),
        ]

    async def get_question_analytics(self) -> List[QuestionAnalyticsDTO]:
        return [
            QuestionAnalyticsDTO(question_id="11111111-1111-1111-1111-111111111111", attempts_count=42, accuracy_rate=0.82, avg_solve_time_seconds=45.0, hint_usage_rate=0.15),
        ]

    async def get_predictions(self, student_id: uuid.UUID) -> PredictionAnalyticsDTO:
        pred_dict = predictive_engine.generate_predictions(str(student_id))
        return PredictionAnalyticsDTO(
            student_id=str(student_id),
            risk_of_failure=pred_dict["risk_of_failure"],
            exam_readiness=pred_dict["exam_readiness"],
            predicted_decay_rate=pred_dict["predicted_decay_rate"],
            expected_mastery_8_days=pred_dict["expected_mastery_8_days"],
            intervention_priority=pred_dict["intervention_priority"],
        )

    async def get_performance_reports(self, student_id: uuid.UUID) -> PerformanceReportDTO:
        sa = await self.get_student_analytics(student_id)
        rep = report_engine.generate_report("student", str(student_id), sa.model_dump())
        return PerformanceReportDTO(
            report_type="student",
            entity_id=str(student_id),
            report_title=rep["report_title"],
            content=rep["content"],
            is_pdf_ready=rep["is_pdf_ready"],
        )
