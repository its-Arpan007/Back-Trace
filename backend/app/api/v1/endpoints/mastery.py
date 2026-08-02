import uuid
from typing import List, Dict, Any
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.mastery import (
    ConceptMasteryDTO,
    StudentMasterySummaryDTO,
    LearningTimelineDTO,
    MasteryPredictionDTO,
    RecalculateMasteryRequest,
    GoalDTO,
    VelocityDTO,
)
from app.services.mastery_service import MasteryService

router = APIRouter(prefix="/mastery", tags=["Student Learning Model (Mastery Engine)"])


@router.get("/student/{student_id}", response_model=BaseResponse[StudentMasterySummaryDTO])
async def get_student_mastery_summary(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[StudentMasterySummaryDTO]:
    service = MasteryService(db)
    summary = await service.get_student_summary(uuid.UUID(student_id))
    return BaseResponse(
        success=True,
        message=f"Mastery summary retrieved for student '{student_id}'",
        code="MASTERY_SUMMARY_RETRIEVED",
        data=summary,
    )


@router.get("/concept/{student_id}/{concept_code}", response_model=BaseResponse[ConceptMasteryDTO])
async def get_concept_mastery(
    student_id: str, concept_code: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[ConceptMasteryDTO]:
    service = MasteryService(db)
    dto = await service.get_concept_mastery(uuid.UUID(student_id), concept_code)
    return BaseResponse(
        success=True,
        message=f"Concept mastery for '{concept_code}' retrieved",
        code="CONCEPT_MASTERY_RETRIEVED",
        data=dto,
    )


@router.get("/timeline/{student_id}", response_model=BaseResponse[LearningTimelineDTO])
async def get_learning_timeline(
    student_id: str, concept_code: str = "DSA_ARRAYS_01", db: AsyncSession = Depends(get_db)
) -> BaseResponse[LearningTimelineDTO]:
    service = MasteryService(db)
    timeline = await service.get_learning_timeline(uuid.UUID(student_id), concept_code)
    return BaseResponse(
        success=True,
        message=f"Learning timeline for concept '{concept_code}' retrieved",
        code="TIMELINE_RETRIEVED",
        data=timeline,
    )


@router.get("/predictions/{student_id}", response_model=BaseResponse[List[MasteryPredictionDTO]])
async def get_mastery_predictions(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[MasteryPredictionDTO]]:
    service = MasteryService(db)
    predictions = await service.get_mastery_predictions(uuid.UUID(student_id))
    return BaseResponse(
        success=True,
        message=f"Mastery predictions generated for student '{student_id}'",
        code="PREDICTIONS_RETRIEVED",
        data=predictions,
    )


@router.get("/history/{student_id}", response_model=BaseResponse[List[Dict[str, Any]]])
async def get_mastery_history(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[Dict[str, Any]]]:
    service = MasteryService(db)
    summary = await service.get_student_summary(uuid.UUID(student_id))
    history_log = [
        {
            "concept_code": m.concept_code,
            "mastery": m.current_mastery,
            "trend": m.mastery_trend,
            "last_practiced": m.last_practiced,
        }
        for m in summary.concept_masteries
    ]
    return BaseResponse(
        success=True,
        message=f"Mastery history log retrieved for student '{student_id}'",
        code="MASTERY_HISTORY_RETRIEVED",
        data=history_log,
    )


@router.get("/statistics/{student_id}", response_model=BaseResponse[Dict[str, Any]])
async def get_student_statistics(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    return BaseResponse(
        success=True,
        message="Student statistics retrieved",
        code="STATISTICS_RETRIEVED",
        data={
            "student_id": student_id,
            "total_questions_solved": 42,
            "overall_accuracy": 0.82,
            "current_streak_days": 7,
            "longest_streak_days": 14,
            "study_frequency_score": 0.95,
            "consistency_score": 0.88,
        },
    )


@router.post("/recalculate", response_model=BaseResponse[StudentMasterySummaryDTO])
async def recalculate_mastery(
    req: RecalculateMasteryRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[StudentMasterySummaryDTO]:
    service = MasteryService(db)
    updated_summary = await service.recalculate_mastery(req)
    return BaseResponse(
        success=True,
        message="Mastery recalculated successfully",
        code="MASTERY_RECALCULATED",
        data=updated_summary,
    )
