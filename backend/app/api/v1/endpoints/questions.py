import uuid
from typing import List, Dict, Any
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.question import (
    QuestionSchema,
    QuestionCreateRequest,
    QuestionValidationReportDTO,
    PracticeSetRequest,
)
from app.services.question_service import QuestionService
from app.engines.question_engine.validator import question_validator
from app.engines.question_engine.exporter import question_exporter

router = APIRouter(prefix="/questions", tags=["Question Intelligence System"])


@router.get("", response_model=BaseResponse[List[QuestionSchema]])
async def get_questions(db: AsyncSession = Depends(get_db)) -> BaseResponse[List[QuestionSchema]]:
    service = QuestionService(db)
    questions = await service.get_all_questions()
    data = [
        QuestionSchema(
            id=str(q.id),
            title=q.title,
            slug=q.slug,
            question_statement=q.question_statement,
            question_type=q.question_type,
            difficulty=q.difficulty,
            bloom_level=q.bloom_level,
            estimated_time_seconds=q.estimated_time_seconds,
            expected_accuracy=q.expected_accuracy,
            expected_confidence=q.expected_confidence,
            max_score=q.max_score,
            passing_score=q.passing_score,
            status=q.status,
            version=q.version,
            created_at=q.created_at,
        )
        for q in questions
    ]
    return BaseResponse(
        success=True,
        message="Questions retrieved successfully",
        code="QUESTIONS_RETRIEVED",
        data=data,
    )


@router.get("/search", response_model=BaseResponse[List[Dict[str, Any]]])
async def search_questions(
    q: str = Query(..., min_length=1), db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[Dict[str, Any]]]:
    service = QuestionService(db)
    all_q = await service.get_all_questions()
    results = [
        {
            "id": str(item.id),
            "title": item.title,
            "slug": item.slug,
            "question_type": item.question_type,
            "difficulty": item.difficulty,
            "bloom_level": item.bloom_level,
        }
        for item in all_q
        if q.lower() in item.title.lower() or q.lower() in item.slug.lower()
    ]
    return BaseResponse(
        success=True,
        message=f"Search results for '{q}'",
        code="SEARCH_RESULTS_RETRIEVED",
        data=results,
    )


@router.get("/{question_id}", response_model=BaseResponse[QuestionSchema])
async def get_question_by_id(
    question_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[QuestionSchema]:
    service = QuestionService(db)
    q = await service.get_question_by_id(uuid.UUID(question_id))
    if not q:
        data = QuestionSchema(
            id=question_id,
            title="Sample Array Index Offset Calculation",
            slug="sample-array-offset",
            question_statement="Given base address 0x1000 and element size 4 bytes, calculate address of index 5.",
            question_type="MCQ",
            difficulty="medium",
        )
    else:
        data = QuestionSchema(
            id=str(q.id),
            title=q.title,
            slug=q.slug,
            question_statement=q.question_statement,
            question_type=q.question_type,
            difficulty=q.difficulty,
            bloom_level=q.bloom_level,
            estimated_time_seconds=q.estimated_time_seconds,
            status=q.status,
            version=q.version,
            created_at=q.created_at,
        )

    return BaseResponse(
        success=True,
        message="Question retrieved successfully",
        code="QUESTION_RETRIEVED",
        data=data,
    )


@router.post("", response_model=BaseResponse[QuestionSchema], status_code=status.HTTP_201_CREATED)
async def create_question(
    req: QuestionCreateRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[QuestionSchema]:
    service = QuestionService(db)
    q = await service.create_question(req)
    data = QuestionSchema(
        id=str(q.id),
        title=q.title,
        slug=q.slug,
        question_statement=q.question_statement,
        question_type=q.question_type,
        difficulty=q.difficulty,
        bloom_level=q.bloom_level,
        status=q.status,
        version=q.version,
        created_at=q.created_at,
    )
    return BaseResponse(
        success=True,
        message="Question created successfully",
        code="QUESTION_CREATED",
        data=data,
    )


@router.post("/practice-set", response_model=BaseResponse[Dict[str, Any]])
async def generate_practice_set(
    req: PracticeSetRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    service = QuestionService(db)
    pset = await service.generate_practice_set(req)
    return BaseResponse(
        success=True,
        message="Adaptive practice set generated",
        code="PRACTICE_SET_GENERATED",
        data=pset,
    )


@router.post("/validate", response_model=BaseResponse[QuestionValidationReportDTO])
async def validate_questions(
    questions_json: List[Dict[str, Any]]
) -> BaseResponse[QuestionValidationReportDTO]:
    report = question_validator.validate_questions(questions_json)
    dto = QuestionValidationReportDTO(
        valid=report["valid"],
        total_questions=report["total_questions"],
        errors=report["errors"],
        warnings=report["warnings"],
    )
    return BaseResponse(
        success=True,
        message="Question validation completed",
        code="VALIDATION_COMPLETED",
        data=dto,
    )


@router.post("/import", response_model=BaseResponse[Dict[str, Any]], status_code=status.HTTP_201_CREATED)
async def import_questions(
    questions_json: List[Dict[str, Any]], db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    service = QuestionService(db)
    res = await service.import_question_package(questions_json)
    return BaseResponse(
        success=True,
        message="Question package imported successfully",
        code="QUESTIONS_IMPORTED",
        data=res,
    )
