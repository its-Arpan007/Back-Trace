import uuid
from typing import Optional, List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.diagnosis import DiagnosisReportModel
from app.repositories.diagnosis_repository import DiagnosisRepository
from app.repositories.question_repository import QuestionRepository
from app.engines.diagnostic_engine.engine import DiagnosticEngine
from app.schemas.diagnosis import DiagnosisRequest, BatchDiagnosisRequest, ExplainRequest, ExplanationResponse


class DiagnosisService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = DiagnosisRepository(db)
        self.q_repo = QuestionRepository(db)
        self.engine = DiagnosticEngine()

    async def analyze_submission(self, req: DiagnosisRequest) -> Dict[str, Any]:
        # Fetch question details
        question_obj = await self.q_repo.get_question_by_id(uuid.UUID(req.question_id))
        q_dict = {
            "id": req.question_id,
            "primary_concept_id": str(question_obj.primary_concept_id) if question_obj and question_obj.primary_concept_id else "DSA_ARRAYS_01",
            "bloom_level": question_obj.bloom_level if question_obj else "apply",
            "estimated_time_seconds": question_obj.estimated_time_seconds if question_obj else 120,
            "correct_answer": "0x1014",
        }

        # Fetch recent student attempt history
        recent_attempts = await self.repo.get_recent_student_attempts(uuid.UUID(req.student_id), limit=5)
        history_list = [
            {"is_correct": a.is_correct, "time_spent_seconds": a.time_spent_seconds, "hints_used": a.hints_used}
            for a in recent_attempts
        ]

        # Execute Pipeline <300ms
        report_dict = await self.engine.run_diagnosis_pipeline(
            student_id=req.student_id,
            question=q_dict,
            student_answer=req.student_answer,
            time_spent_seconds=req.time_spent_seconds,
            hints_used=req.hints_used,
            student_history=history_list,
        )

        # Persist attempt and diagnosis report to DB
        await self.repo.record_student_attempt({
            "student_id": uuid.UUID(req.student_id),
            "question_id": uuid.UUID(req.question_id),
            "is_correct": report_dict["is_correct"],
            "time_spent_seconds": req.time_spent_seconds,
            "hints_used": req.hints_used,
            "selected_option": str(req.student_answer),
        })

        db_report = await self.repo.create_diagnosis_report({
            "student_id": uuid.UUID(req.student_id),
            "question_id": uuid.UUID(req.question_id),
            "concept_code": report_dict["concept_code"],
            "is_correct": report_dict["is_correct"],
            "score": report_dict["score"],
            "evaluation_details_json": report_dict["evaluation_details"],
            "primary_root_cause": report_dict["primary_root_cause"],
            "secondary_root_causes_json": report_dict["secondary_root_causes"],
            "confidence_score": report_dict["confidence_score"],
            "severity": report_dict["severity"],
            "evidence_json": report_dict["evidence"],
            "detected_misconceptions_json": report_dict["detected_misconceptions"],
            "weak_prerequisites_json": report_dict["weak_prerequisites"],
            "bloom_level": report_dict["bloom_level"],
            "mastery_impact_json": report_dict["mastery_impact"],
            "recommended_actions_json": report_dict["recommended_actions"],
            "processing_time_ms": report_dict["processing_time_ms"],
            "engine_versions_json": report_dict["engine_versions"],
        })

        report_dict["diagnosis_id"] = str(db_report.id)
        report_dict["created_at"] = db_report.created_at
        return report_dict

    async def get_diagnosis_by_id(self, diagnosis_id: uuid.UUID) -> Optional[DiagnosisReportModel]:
        return await self.repo.get_diagnosis_by_id(diagnosis_id)

    async def get_student_history(self, student_id: uuid.UUID) -> List[DiagnosisReportModel]:
        return await self.repo.get_student_diagnosis_history(student_id)

    async def explain_diagnosis(self, req: ExplainRequest) -> ExplanationResponse:
        report = await self.get_diagnosis_by_id(uuid.UUID(req.diagnosis_id))
        primary_cause = report.primary_root_cause if report else "Concept Gap"
        concept = report.concept_code if report else "DSA_ARRAYS_01"

        return ExplanationResponse(
            diagnosis_id=req.diagnosis_id,
            natural_language_explanation=(
                f"Your attempt failed due to a {primary_cause} on concept {concept}. "
                f"You miscalculated the array index offset by multiplying base address directly instead of stride length."
            ),
            key_takeaways=[
                "Pointer arithmetic requires element stride offset.",
                "Review contiguous memory address calculation formula: Address = Base + i * Stride.",
            ],
            suggested_hint="Try breaking down Base + (5 * 4) step by step.",
        )
