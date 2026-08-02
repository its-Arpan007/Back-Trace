import uuid
from typing import List, Dict, Any
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.recommendation import (
    RecommendationDTO,
    LearningPlanDTO,
    WeeklyLearningPlanDTO,
    RevisionScheduleDTO,
    ResourceRecommendationDTO,
    QuestionRecommendationDTO,
    GoalRecommendationDTO,
    RecommendationFeedbackRequest,
    GenerateRecommendationsRequest,
)
from app.services.recommendation_service import RecommendationService

router = APIRouter(prefix="/recommendations", tags=["Adaptive Recommendation Engine"])


@router.get("/student/{student_id}", response_model=BaseResponse[List[RecommendationDTO]])
async def get_student_recommendations(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[RecommendationDTO]]:
    service = RecommendationService(db)
    recs = await service.get_student_recommendations(uuid.UUID(student_id))
    return BaseResponse(
        success=True,
        message=f"Personalized recommendations retrieved for student '{student_id}'",
        code="RECOMMENDATIONS_RETRIEVED",
        data=recs,
    )


@router.get("/today/{student_id}", response_model=BaseResponse[LearningPlanDTO])
async def get_todays_learning_plan(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[LearningPlanDTO]:
    service = RecommendationService(db)
    plan = await service.get_todays_plan(uuid.UUID(student_id))
    return BaseResponse(
        success=True,
        message="Today's personalized learning plan retrieved",
        code="TODAYS_PLAN_RETRIEVED",
        data=plan,
    )


@router.get("/weekly/{student_id}", response_model=BaseResponse[WeeklyLearningPlanDTO])
async def get_weekly_learning_plan(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[WeeklyLearningPlanDTO]:
    service = RecommendationService(db)
    plan = await service.get_weekly_plan(uuid.UUID(student_id))
    return BaseResponse(
        success=True,
        message="Weekly learning plan retrieved",
        code="WEEKLY_PLAN_RETRIEVED",
        data=plan,
    )


@router.get("/revision/{student_id}", response_model=BaseResponse[List[RevisionScheduleDTO]])
async def get_revision_schedule(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[RevisionScheduleDTO]]:
    service = RecommendationService(db)
    revs = await service.get_revision_schedule(uuid.UUID(student_id))
    return BaseResponse(
        success=True,
        message="Spaced revision schedule retrieved",
        code="REVISION_SCHEDULE_RETRIEVED",
        data=revs,
    )


@router.get("/resources/{student_id}", response_model=BaseResponse[List[ResourceRecommendationDTO]])
async def get_recommended_resources(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[ResourceRecommendationDTO]]:
    service = RecommendationService(db)
    res_list = await service.get_recommended_resources(uuid.UUID(student_id))
    return BaseResponse(
        success=True,
        message="Educational learning resources retrieved",
        code="RESOURCES_RETRIEVED",
        data=res_list,
    )


@router.get("/questions/{student_id}", response_model=BaseResponse[List[QuestionRecommendationDTO]])
async def get_recommended_questions(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[QuestionRecommendationDTO]]:
    service = RecommendationService(db)
    q_list = await service.get_recommended_questions(uuid.UUID(student_id))
    return BaseResponse(
        success=True,
        message="Targeted practice questions retrieved",
        code="QUESTIONS_RETRIEVED",
        data=q_list,
    )


@router.get("/goals/{student_id}", response_model=BaseResponse[List[GoalRecommendationDTO]])
async def get_recommended_goals(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[GoalRecommendationDTO]]:
    service = RecommendationService(db)
    g_list = await service.get_recommended_goals(uuid.UUID(student_id))
    return BaseResponse(
        success=True,
        message="Actionable learning goals retrieved",
        code="GOALS_RETRIEVED",
        data=g_list,
    )


@router.post("/feedback", response_model=BaseResponse[Dict[str, Any]])
async def submit_recommendation_feedback(
    req: RecommendationFeedbackRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    service = RecommendationService(db)
    res = await service.log_feedback(req)
    return BaseResponse(
        success=True,
        message="Recommendation feedback recorded",
        code="FEEDBACK_LOGGED",
        data=res,
    )


@router.post("/generate", response_model=BaseResponse[Dict[str, Any]])
async def generate_recommendations_endpoint(
    req: GenerateRecommendationsRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    service = RecommendationService(db)
    gen_res = await service.generate_fresh_recommendations(req)
    return BaseResponse(
        success=True,
        message="Fresh personalized recommendations generated",
        code="RECOMMENDATIONS_GENERATED",
        data=gen_res,
    )
