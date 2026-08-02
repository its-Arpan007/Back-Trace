import uuid
from typing import List, Dict, Any
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.teacher import (
    ClassSummaryDTO,
    ClassAnalyticsDTO,
    InterventionCandidateDTO,
    AssessmentBuildRequest,
    AssignmentCreateRequest,
)
from app.services.teacher_service import TeacherService

router = APIRouter(prefix="/teacher", tags=["Teacher Intelligence Platform"])


@router.get("/classes", response_model=BaseResponse[List[ClassSummaryDTO]])
async def get_teacher_classes(
    teacher_id: str = "11111111-1111-1111-1111-111111111111", db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[ClassSummaryDTO]]:
    service = TeacherService(db)
    dtos = await service.get_teacher_classes(uuid.UUID(teacher_id))
    return BaseResponse(
        success=True,
        message="Teacher classes retrieved successfully",
        code="TEACHER_CLASSES_RETRIEVED",
        data=dtos,
    )


@router.get("/classes/{class_id}/analytics", response_model=BaseResponse[ClassAnalyticsDTO])
async def get_class_analytics(
    class_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[ClassAnalyticsDTO]:
    service = TeacherService(db)
    dto = await service.get_class_analytics(class_id)
    return BaseResponse(
        success=True,
        message=f"Class analytics retrieved for '{class_id}'",
        code="CLASS_ANALYTICS_RETRIEVED",
        data=dto,
    )


@router.get("/interventions", response_model=BaseResponse[List[InterventionCandidateDTO]])
async def get_intervention_candidates(
    teacher_id: str = "11111111-1111-1111-1111-111111111111", db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[InterventionCandidateDTO]]:
    service = TeacherService(db)
    dtos = await service.get_intervention_candidates(uuid.UUID(teacher_id))
    return BaseResponse(
        success=True,
        message="High-risk intervention candidates retrieved",
        code="INTERVENTIONS_RETRIEVED",
        data=dtos,
    )


@router.post("/assessments", response_model=BaseResponse[Dict[str, Any]])
async def build_assessment_endpoint(
    req: AssessmentBuildRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    service = TeacherService(db)
    res = await service.build_assessment(req)
    return BaseResponse(
        success=True,
        message="Assessment generated from Knowledge Graph nodes",
        code="ASSESSMENT_CREATED",
        data=res,
    )


@router.post("/assignments", response_model=BaseResponse[Dict[str, Any]])
async def create_assignment_endpoint(
    req: AssignmentCreateRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    service = TeacherService(db)
    res = await service.create_assignment(req)
    return BaseResponse(
        success=True,
        message="Assignment scheduled for class",
        code="ASSIGNMENT_CREATED",
        data=res,
    )


@router.get("/reports", response_model=BaseResponse[Dict[str, Any]])
async def get_teacher_reports(
    teacher_id: str = "11111111-1111-1111-1111-111111111111", db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    return BaseResponse(
        success=True,
        message="Class and student reports compiled",
        code="TEACHER_REPORTS_COMPILED",
        data={
            "teacher_id": teacher_id,
            "reports": [
                {"report_id": "rep_class_01", "title": "Class Weakness Matrix", "type": "pdf", "is_ready": True},
                {"report_id": "rep_misconception_01", "title": "Top Misconception Frequency Audit", "type": "csv", "is_ready": True},
            ]
        },
    )
