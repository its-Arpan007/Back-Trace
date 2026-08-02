from typing import Dict, Any, List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.graph import GraphImportRequest, ValidationReportDTO
from app.services.curriculum_service import CurriculumService
from app.curriculum.validator import curriculum_validator

router = APIRouter(prefix="/graph", tags=["Knowledge Graph Engine"])


@router.get("", response_model=BaseResponse[Dict[str, Any]])
async def get_graph(db: AsyncSession = Depends(get_db)) -> BaseResponse[Dict[str, Any]]:
    service = CurriculumService(db)
    graph_data = await service.get_full_graph()
    return BaseResponse(
        success=True,
        message="Knowledge Graph retrieved",
        code="GRAPH_RETRIEVED",
        data=graph_data,
    )


@router.get("/dependencies/{concept_code}", response_model=BaseResponse[Dict[str, Any]])
async def get_dependencies(
    concept_code: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    service = CurriculumService(db)
    deps = await service.get_concept_dependencies(concept_code)
    return BaseResponse(
        success=True,
        message=f"Dependencies for '{concept_code}' retrieved",
        code="DEPENDENCIES_RETRIEVED",
        data=deps,
    )


@router.get("/learning-path/{concept_code}", response_model=BaseResponse[Dict[str, Any]])
async def get_learning_path(
    concept_code: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    service = CurriculumService(db)
    deps = await service.get_concept_dependencies(concept_code)
    return BaseResponse(
        success=True,
        message=f"Learning path for '{concept_code}' generated",
        code="LEARNING_PATH_GENERATED",
        data={
            "target_concept": concept_code,
            "optimal_sequence": deps["optimal_learning_path"],
        },
    )


@router.get("/prerequisites/{concept_code}", response_model=BaseResponse[Dict[str, Any]])
async def get_prerequisites(
    concept_code: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    service = CurriculumService(db)
    deps = await service.get_concept_dependencies(concept_code)
    return BaseResponse(
        success=True,
        message=f"Prerequisites for '{concept_code}' retrieved",
        code="PREREQUISITES_RETRIEVED",
        data={"concept_code": concept_code, "prerequisites": deps["parents"]},
    )


@router.post("/validate", response_model=BaseResponse[ValidationReportDTO])
async def validate_graph(
    graph_req: GraphImportRequest,
) -> BaseResponse[ValidationReportDTO]:
    report = curriculum_validator.validate_graph(
        graph_data=graph_req.graph_json,
        concepts_list=graph_req.concepts_json,
    )
    dto = ValidationReportDTO(
        valid=report["valid"],
        domain=report["domain"],
        graph_version=report["graph_version"],
        total_concepts=report["total_concepts"],
        total_edges=report["total_edges"],
        errors=report["errors"],
        warnings=report["warnings"],
    )
    return BaseResponse(
        success=True,
        message="Graph validation completed",
        code="VALIDATION_COMPLETED",
        data=dto,
    )


@router.post("/import", response_model=BaseResponse[Dict[str, Any]], status_code=status.HTTP_201_CREATED)
async def import_curriculum(
    req: GraphImportRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[Dict[str, Any]]:
    service = CurriculumService(db)
    res = await service.import_curriculum_package(
        domain=req.domain,
        graph_json=req.graph_json,
        concepts_json=req.concepts_json,
    )
    return BaseResponse(
        success=True,
        message=f"Curriculum imported successfully for domain '{req.domain}'",
        code="CURRICULUM_IMPORTED",
        data=res,
    )
