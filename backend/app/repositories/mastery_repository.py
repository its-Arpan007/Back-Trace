import uuid
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.mastery import (
    ConceptMasteryModel,
    ConceptHistoryModel,
    LearningSessionModel,
    LearningEventModel,
    LearningVelocityModel,
    KnowledgeDecayModel,
    MasterySnapshotModel,
    MasteryPredictionModel,
    StudentStatisticsModel,
    LearningGoalModel,
    LearningStreakModel,
)


class MasteryRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_concept_mastery(self, student_id: uuid.UUID, concept_code: str) -> Optional[ConceptMasteryModel]:
        query = select(ConceptMasteryModel).where(
            ConceptMasteryModel.student_id == student_id,
            ConceptMasteryModel.concept_code == concept_code,
            ConceptMasteryModel.deleted_at == None,
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_all_student_masteries(self, student_id: uuid.UUID) -> List[ConceptMasteryModel]:
        query = select(ConceptMasteryModel).where(
            ConceptMasteryModel.student_id == student_id,
            ConceptMasteryModel.deleted_at == None,
        )
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def upsert_concept_mastery(self, student_id: uuid.UUID, concept_code: str, data: Dict[str, Any]) -> ConceptMasteryModel:
        cm = await self.get_concept_mastery(student_id, concept_code)
        if not cm:
            cm = ConceptMasteryModel(student_id=student_id, concept_code=concept_code, **data)
            self.session.add(cm)
        else:
            for key, val in data.items():
                setattr(cm, key, val)
            self.session.add(cm)

        await self.session.flush()
        return cm

    async def add_history_record(self, student_id: uuid.UUID, concept_code: str, before: float, after: float, reason: str) -> ConceptHistoryModel:
        hist = ConceptHistoryModel(
            student_id=student_id,
            concept_code=concept_code,
            mastery_before=before,
            mastery_after=after,
            change_reason=reason,
        )
        self.session.add(hist)
        await self.session.flush()
        return hist

    async def get_concept_history(self, student_id: uuid.UUID, concept_code: str) -> List[ConceptHistoryModel]:
        query = (
            select(ConceptHistoryModel)
            .where(ConceptHistoryModel.student_id == student_id, ConceptHistoryModel.concept_code == concept_code)
            .order_by(ConceptHistoryModel.created_at.asc())
        )
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def log_learning_event(self, student_id: uuid.UUID, event_type: str, payload: Dict[str, Any]) -> LearningEventModel:
        ev = LearningEventModel(student_id=student_id, event_type=event_type, payload_json=payload)
        self.session.add(ev)
        await self.session.flush()
        return ev

    async def get_student_velocity(self, student_id: uuid.UUID) -> Optional[LearningVelocityModel]:
        query = select(LearningVelocityModel).where(LearningVelocityModel.student_id == student_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_student_decay(self, student_id: uuid.UUID, concept_code: str) -> Optional[KnowledgeDecayModel]:
        query = select(KnowledgeDecayModel).where(
            KnowledgeDecayModel.student_id == student_id, KnowledgeDecayModel.concept_code == concept_code
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_student_predictions(self, student_id: uuid.UUID) -> List[MasteryPredictionModel]:
        query = select(MasteryPredictionModel).where(MasteryPredictionModel.student_id == student_id)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def get_student_statistics(self, student_id: uuid.UUID) -> Optional[StudentStatisticsModel]:
        query = select(StudentStatisticsModel).where(StudentStatisticsModel.student_id == student_id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_student_goals(self, student_id: uuid.UUID) -> List[LearningGoalModel]:
        query = select(LearningGoalModel).where(LearningGoalModel.student_id == student_id)
        result = await self.session.execute(query)
        return list(result.scalars().all())
