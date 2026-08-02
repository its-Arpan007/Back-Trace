import uuid
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.curriculum import ChapterSchema, ChapterCreateRequest
from app.services.curriculum_service import CurriculumService

router = APIRouter(prefix="/chapters", tags=["Curriculum - Chapters"])


@router.get("", response_model=BaseResponse[List[ChapterSchema]])
async def get_chapters(
    subject_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[ChapterSchema]]:
    service = CurriculumService(db)
    chapters = await service.get_chapters_by_subject(uuid.UUID(subject_id))
    data = [
        ChapterSchema(
            id=str(c.id),
            subject_id=str(c.subject_id),
            name=c.name,
            description=c.description,
            order=c.order,
            estimated_hours=c.estimated_hours,
            difficulty=c.difficulty,
            version=c.version,
        )
        for c in chapters
    ]
    return BaseResponse(
        success=True,
        message="Chapters retrieved successfully",
        code="CHAPTERS_RETRIEVED",
        data=data,
    )


@router.post("", response_model=BaseResponse[ChapterSchema], status_code=status.HTTP_201_CREATED)
async def create_chapter(
    req: ChapterCreateRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[ChapterSchema]:
    service = CurriculumService(db)
    c = await service.create_chapter(req)
    data = ChapterSchema(
        id=str(c.id),
        subject_id=str(c.subject_id),
        name=c.name,
        description=c.description,
        order=c.order,
        estimated_hours=c.estimated_hours,
        difficulty=c.difficulty,
        version=c.version,
    )
    return BaseResponse(
        success=True,
        message="Chapter created successfully",
        code="CHAPTER_CREATED",
        data=data,
    )
