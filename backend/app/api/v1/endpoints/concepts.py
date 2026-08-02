import uuid
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.curriculum import ConceptSchema, ConceptCreateRequest
from app.services.curriculum_service import CurriculumService

router = APIRouter(prefix="/concepts", tags=["Curriculum - Concepts"])


@router.get("", response_model=BaseResponse[List[ConceptSchema]])
async def get_concepts(
    topic_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[ConceptSchema]]:
    service = CurriculumService(db)
    concepts = await service.get_concepts_by_topic(uuid.UUID(topic_id))
    data = [
        ConceptSchema(
            id=str(c.id),
            topic_id=str(c.topic_id),
            concept_code=c.concept_code,
            title=c.title,
            description=c.description,
            difficulty=c.difficulty,
            bloom_level=c.bloom_level,
            estimated_learning_time_minutes=c.estimated_learning_time_minutes,
            mastery_threshold=c.mastery_threshold,
            status=c.status,
            version=c.version,
            created_at=c.created_at,
        )
        for c in concepts
    ]
    return BaseResponse(
        success=True,
        message="Concepts retrieved successfully",
        code="CONCEPTS_RETRIEVED",
        data=data,
    )


@router.post("", response_model=BaseResponse[ConceptSchema], status_code=status.HTTP_201_CREATED)
async def create_concept(
    req: ConceptCreateRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[ConceptSchema]:
    service = CurriculumService(db)
    c = await service.create_concept(req)
    data = ConceptSchema(
        id=str(c.id),
        topic_id=str(c.topic_id),
        concept_code=c.concept_code,
        title=c.title,
        description=c.description,
        difficulty=c.difficulty,
        bloom_level=c.bloom_level,
        estimated_learning_time_minutes=c.estimated_learning_time_minutes,
        mastery_threshold=c.mastery_threshold,
        status=c.status,
        version=c.version,
        created_at=c.created_at,
    )
    return BaseResponse(
        success=True,
        message="Concept created successfully",
        code="CONCEPT_CREATED",
        data=data,
    )
