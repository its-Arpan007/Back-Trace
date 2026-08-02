import uuid
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.analytics import (
    AnalyticsEventModel,
    AnalyticsSnapshotModel,
    StudentAnalyticsModel,
    TeacherAnalyticsModel,
    InstitutionAnalyticsModel,
    ConceptAnalyticsModel,
    QuestionAnalyticsModel,
    RecommendationAnalyticsModel,
    PredictionAnalyticsModel,
    PerformanceReportModel,
)


class AnalyticsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def log_analytics_event(self, student_id: uuid.UUID, event_type: str, payload: Dict[str, Any]) -> AnalyticsEventModel:
        ev = AnalyticsEventModel(student_id=student_id, event_type=event_type, payload_json=payload)
        self.session.add(ev)
        await self.session.flush()
        return ev

    async def get_student_analytics(self, student_id: uuid.UUID) -> Optional[StudentAnalyticsModel]:
        query = select(StudentAnalyticsModel).where(StudentAnalyticsModel.student_id == student_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def upsert_student_analytics(self, student_id: uuid.UUID, data: Dict[str, Any]) -> StudentAnalyticsModel:
        sa = await self.get_student_analytics(student_id)
        if not sa:
            sa = StudentAnalyticsModel(student_id=student_id, **data)
            self.session.add(sa)
        else:
            for k, v in data.items():
                setattr(sa, k, v)
            self.session.add(sa)
        await self.session.flush()
        return sa

    async def get_teacher_analytics(self, teacher_id: uuid.UUID) -> Optional[TeacherAnalyticsModel]:
        query = select(TeacherAnalyticsModel).where(TeacherAnalyticsModel.teacher_id == teacher_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_institution_analytics(self, institution_id: uuid.UUID) -> Optional[InstitutionAnalyticsModel]:
        query = select(InstitutionAnalyticsModel).where(InstitutionAnalyticsModel.institution_id == institution_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_all_concept_analytics(self) -> List[ConceptAnalyticsModel]:
        query = select(ConceptAnalyticsModel)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def get_all_question_analytics(self) -> List[QuestionAnalyticsModel]:
        query = select(QuestionAnalyticsModel)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def save_performance_report(self, data: Dict[str, Any]) -> PerformanceReportModel:
        rep = PerformanceReportModel(**data)
        self.session.add(rep)
        await self.session.flush()
        return rep
