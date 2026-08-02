import uuid
from typing import List, Dict, Any
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.base import BaseResponse
from app.schemas.diagnosis import (
    DiagnosisRequest,
    BatchDiagnosisRequest,
    DiagnosisReportDTO,
    ExplainRequest,
    ExplanationResponse,
)
from app.services.diagnosis_service import DiagnosisService

router = APIRouter(prefix="/diagnosis", tags=["BACKTRACE Intelligence Engine"])


@router.post("/analyze", response_model=BaseResponse[DiagnosisReportDTO])
async def analyze_submission(
    req: DiagnosisRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[DiagnosisReportDTO]:
    service = DiagnosisService(db)
    report_dict = await service.analyze_submission(req)
    dto = DiagnosisReportDTO(**report_dict)
    return BaseResponse(
        success=True,
        message="Diagnosis report generated successfully",
        code="DIAGNOSIS_COMPLETED",
        data=dto,
    )


@router.post("/batch", response_model=BaseResponse[List[DiagnosisReportDTO]])
async def analyze_batch(
    req: BatchDiagnosisRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[DiagnosisReportDTO]]:
    service = DiagnosisService(db)
    reports = []
    for sub in req.submissions:
        rep = await service.analyze_submission(sub)
        reports.append(DiagnosisReportDTO(**rep))
    return BaseResponse(
        success=True,
        message=f"Batch diagnosis completed for {len(reports)} submissions",
        code="BATCH_DIAGNOSIS_COMPLETED",
        data=reports,
    )


@router.get("/{diagnosis_id}", response_model=BaseResponse[DiagnosisReportDTO])
async def get_diagnosis_by_id(
    diagnosis_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[DiagnosisReportDTO]:
    service = DiagnosisService(db)
    rep = await service.get_diagnosis_by_id(uuid.UUID(diagnosis_id))
    if not rep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Diagnosis report not found")

    dto = DiagnosisReportDTO(
        diagnosis_id=str(rep.id),
        student_id=str(rep.student_id),
        question_id=str(rep.question_id),
        concept_code=rep.concept_code,
        is_correct=rep.is_correct,
        score=rep.score,
        evaluation_details=rep.evaluation_details_json,
        primary_root_cause=rep.primary_root_cause,
        secondary_root_causes=rep.secondary_root_causes_json,
        confidence_score=rep.confidence_score,
        severity=rep.severity,
        evidence=rep.evidence_json,
        detected_misconceptions=rep.detected_misconceptions_json,
        weak_prerequisites=rep.weak_prerequisites_json,
        bloom_level=rep.bloom_level,
        mastery_impact=rep.mastery_impact_json,
        recommended_actions=rep.recommended_actions_json,
        processing_time_ms=rep.processing_time_ms,
        engine_versions=rep.engine_versions_json,
        created_at=rep.created_at,
    )
    return BaseResponse(
        success=True,
        message="Diagnosis report retrieved",
        code="DIAGNOSIS_RETRIEVED",
        data=dto,
    )


@router.get("/student/{student_id}", response_model=BaseResponse[List[DiagnosisReportDTO]])
async def get_student_diagnoses(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[DiagnosisReportDTO]]:
    service = DiagnosisService(db)
    reports = await service.get_student_history(uuid.UUID(student_id))
    dtos = [
        DiagnosisReportDTO(
            diagnosis_id=str(rep.id),
            student_id=str(rep.student_id),
            question_id=str(rep.question_id),
            concept_code=rep.concept_code,
            is_correct=rep.is_correct,
            score=rep.score,
            primary_root_cause=rep.primary_root_cause,
            confidence_score=rep.confidence_score,
            severity=rep.severity,
            processing_time_ms=rep.processing_time_ms,
            created_at=rep.created_at,
        )
        for rep in reports
    ]
    return BaseResponse(
        success=True,
        message=f"Diagnosis history retrieved for student {student_id}",
        code="STUDENT_DIAGNOSES_RETRIEVED",
        data=dtos,
    )


@router.get("/history/{student_id}", response_model=BaseResponse[List[DiagnosisReportDTO]])
async def get_student_history_alias(
    student_id: str, db: AsyncSession = Depends(get_db)
) -> BaseResponse[List[DiagnosisReportDTO]]:
    return await get_student_diagnoses(student_id, db)


@router.post("/explain", response_model=BaseResponse[ExplanationResponse])
async def explain_diagnosis(
    req: ExplainRequest, db: AsyncSession = Depends(get_db)
) -> BaseResponse[ExplanationResponse]:
    service = DiagnosisService(db)
    explanation = await service.explain_diagnosis(req)
    return BaseResponse(
        success=True,
        message="Natural language explanation generated",
        code="EXPLANATION_GENERATED",
        data=explanation,
    )
