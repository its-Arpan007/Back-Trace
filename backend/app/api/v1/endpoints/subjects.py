import uuid
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.curriculum import SubjectSchema, SubjectCreateRequest
from app.services.curriculum_service import CurriculumService

router = APIRouter(prefix="/subjects", tags=["Curriculum - Subjects"])


@router.get("", response_model=BaseResponse[List[SubjectSchema]])
async def get_subjects(db: AsyncSession = Depends(get_db)) -> BaseResponse[List[SubjectSchema]]:
    service = CurriculumService(db)
    subjects = await service.get_all_subjects()
    data = [
        SubjectSchema(
            id=str(s.id),
            name=s.name,
            code=s.code,
            description=s.description,
            icon=s.icon,
            color=s.color,
            difficulty_scale=s.difficulty_scale,
            status=s.status,
            version=s.version,
            created_at=s.created_at,
        )
        for s in subjects
    ]
    return BaseResponse(
        success=True,
        message="Subjects retrieved successfully",
        code="SUBJECTS_RETRIEVED",
        data=data,
    )


@router.post("", response_model=BaseResponse[SubjectSchema], status_code=status.HTTP_201_CREATED)
async def create_subject(
    req: SubjectCreateRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[SubjectSchema]:
    service = CurriculumService(db)
    s = await service.create_subject(req)
    data = SubjectSchema(
        id=str(s.id),
        name=s.name,
        code=s.code,
        description=s.description,
        icon=s.icon,
        color=s.color,
        difficulty_scale=s.difficulty_scale,
        status=s.status,
        version=s.version,
        created_at=s.created_at,
    )
    return BaseResponse(
        success=True,
        message="Subject created successfully",
        code="SUBJECT_CREATED",
        data=data,
    )
