import uuid
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.recommendation import (
    RecommendationModel,
    RecommendationHistoryModel,
    RecommendationFeedbackModel,
    LearningPlanModel,
    DailyLearningPlanModel,
    WeeklyLearningPlanModel,
    RevisionScheduleModel,
    ResourceRecommendationModel,
    GoalRecommendationModel,
    RecommendationStatisticsModel,
)


class RecommendationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_recommendation(self, data: Dict[str, Any]) -> RecommendationModel:
        rec = RecommendationModel(**data)
        self.session.add(rec)
        await self.session.flush()
        return rec

    async def get_student_recommendations(self, student_id: uuid.UUID, limit: int = 10) -> List[RecommendationModel]:
        query = (
            select(RecommendationModel)
            .where(
                RecommendationModel.student_id == student_id,
                RecommendationModel.is_dismissed == False,
                RecommendationModel.deleted_at == None,
            )
            .order_by(RecommendationModel.priority_score.desc())
            .limit(limit)
        )
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def log_feedback(self, student_id: uuid.UUID, rec_id: uuid.UUID, rating: int, text: str, action: str) -> RecommendationFeedbackModel:
        fb = RecommendationFeedbackModel(
            student_id=student_id,
            recommendation_id=rec_id,
            rating_score=rating,
            feedback_text=text,
        )
        self.session.add(fb)

        hist = RecommendationHistoryModel(
            student_id=student_id,
            recommendation_id=rec_id,
            action_taken=action,
        )
        self.session.add(hist)
        await self.session.flush()
        return fb

    async def save_learning_plan(self, data: Dict[str, Any]) -> LearningPlanModel:
        plan = LearningPlanModel(**data)
        self.session.add(plan)
        await self.session.flush()
        return plan

    async def get_active_plan(self, student_id: uuid.UUID, plan_type: str = "today") -> Optional[LearningPlanModel]:
        query = select(LearningPlanModel).where(
            LearningPlanModel.student_id == student_id,
            LearningPlanModel.plan_type == plan_type,
            LearningPlanModel.is_active == True,
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_revision_schedules(self, student_id: uuid.UUID) -> List[RevisionScheduleModel]:
        query = (
            select(RevisionScheduleModel)
            .where(RevisionScheduleModel.student_id == student_id, RevisionScheduleModel.is_completed == False)
            .order_by(RevisionScheduleModel.scheduled_date.asc())
        )
        result = await self.session.execute(query)
        return list(result.scalars().all())
