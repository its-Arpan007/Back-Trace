import uuid
from typing import Optional, List, Dict, Any
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.diagnosis import (
    DiagnosisReportModel,
    DiagnosticRuleModel,
    EvidenceRecordModel,
    StudentAttemptHistoryModel,
)


class DiagnosisRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_diagnosis_report(self, data: Dict[str, Any]) -> DiagnosisReportModel:
        evidence_list = data.pop("evidence_json", [])
        report = DiagnosisReportModel(**data)
        report.evidence_json = evidence_list
        self.session.add(report)
        await self.session.flush()

        for ev in evidence_list:
            if isinstance(ev, dict):
                rec = EvidenceRecordModel(
                    diagnosis_id=report.id,
                    evidence_source=ev.get("source", "system"),
                    description=ev.get("description", ""),
                    weight=ev.get("weight", 1.0),
                    details_json=ev.get("details", {}),
                )
                self.session.add(rec)
        await self.session.flush()
        return report

    async def get_diagnosis_by_id(self, diagnosis_id: uuid.UUID) -> Optional[DiagnosisReportModel]:
        query = (
            select(DiagnosisReportModel)
            .where(DiagnosisReportModel.id == diagnosis_id)
            .options(selectinload(DiagnosisReportModel.evidence_records))
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_student_diagnosis_history(self, student_id: uuid.UUID) -> List[DiagnosisReportModel]:
        query = (
            select(DiagnosisReportModel)
            .where(DiagnosisReportModel.student_id == student_id)
            .order_by(DiagnosisReportModel.created_at.desc())
        )
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def get_question_diagnosis_history(self, question_id: uuid.UUID) -> List[DiagnosisReportModel]:
        query = (
            select(DiagnosisReportModel)
            .where(DiagnosisReportModel.question_id == question_id)
            .order_by(DiagnosisReportModel.created_at.desc())
        )
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def record_student_attempt(self, data: Dict[str, Any]) -> StudentAttemptHistoryModel:
        attempt = StudentAttemptHistoryModel(**data)
        self.session.add(attempt)
        await self.session.flush()
        return attempt

    async def get_recent_student_attempts(self, student_id: uuid.UUID, limit: int = 10) -> List[StudentAttemptHistoryModel]:
        query = (
            select(StudentAttemptHistoryModel)
            .where(StudentAttemptHistoryModel.student_id == student_id)
            .order_by(StudentAttemptHistoryModel.created_at.desc())
            .limit(limit)
        )
        result = await self.session.execute(query)
        return list(result.scalars().all())
