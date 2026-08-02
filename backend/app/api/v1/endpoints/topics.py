import uuid
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.curriculum import TopicSchema, TopicCreateRequest
from app.services.curriculum_service import CurriculumService

router = APIRouter(prefix="/topics", tags=["Curriculum - Topics"])


@router.get("", response_model=BaseResponse[List[TopicSchema]])
async def get_topics(
    chapter_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[TopicSchema]]:
    service = CurriculumService(db)
    topics = await service.get_topics_by_chapter(uuid.UUID(chapter_id))
    data = [
        TopicSchema(
            id=str(t.id),
            chapter_id=str(t.chapter_id),
            name=t.name,
            description=t.description,
            order=t.order,
            difficulty=t.difficulty,
            version=t.version,
        )
        for t in topics
    ]
    return BaseResponse(
        success=True,
        message="Topics retrieved successfully",
        code="TOPICS_RETRIEVED",
        data=data,
    )


@router.post("", response_model=BaseResponse[TopicSchema], status_code=status.HTTP_201_CREATED)
async def create_topic(
    req: TopicCreateRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[TopicSchema]:
    service = CurriculumService(db)
    t = await service.create_topic(req)
    data = TopicSchema(
        id=str(t.id),
        chapter_id=str(t.chapter_id),
        name=t.name,
        description=t.description,
        order=t.order,
        difficulty=t.difficulty,
        version=t.version,
    )
    return BaseResponse(
        success=True,
        message="Topic created successfully",
        code="TOPIC_CREATED",
        data=data,
    )
