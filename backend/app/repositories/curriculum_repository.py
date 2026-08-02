import uuid
from typing import Optional, List, Dict, Any
from sqlalchemy import select, update, delete, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.curriculum import (
    SubjectModel,
    ChapterModel,
    TopicModel,
    ConceptModel,
    LearningObjectiveModel,
    ConceptRelationshipModel,
    MisconceptionModel,
    ResourceModel,
    GraphNodeModel,
    GraphEdgeModel,
    LearningPathModel,
    ConceptAliasModel,
)
from app.repositories.base import BaseRepository


class CurriculumRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    # Subject Methods
    async def get_all_subjects(self) -> List[SubjectModel]:
        query = select(SubjectModel).where(SubjectModel.deleted_at == None).options(selectinload(SubjectModel.chapters))
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def get_subject_by_id(self, subject_id: uuid.UUID) -> Optional[SubjectModel]:
        query = select(SubjectModel).where(SubjectModel.id == subject_id, SubjectModel.deleted_at == None).options(
            selectinload(SubjectModel.chapters).selectinload(ChapterModel.topics)
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def create_subject(self, data: Dict[str, Any]) -> SubjectModel:
        subj = SubjectModel(**data)
        self.session.add(subj)
        await self.session.flush()
        return subj

    # Chapter Methods
    async def get_chapters_by_subject(self, subject_id: uuid.UUID) -> List[ChapterModel]:
        query = select(ChapterModel).where(ChapterModel.subject_id == subject_id, ChapterModel.deleted_at == None).order_by(ChapterModel.order)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def create_chapter(self, data: Dict[str, Any]) -> ChapterModel:
        chap = ChapterModel(**data)
        self.session.add(chap)
        await self.session.flush()
        return chap

    # Topic Methods
    async def get_topics_by_chapter(self, chapter_id: uuid.UUID) -> List[TopicModel]:
        query = select(TopicModel).where(TopicModel.chapter_id == chapter_id, TopicModel.deleted_at == None).order_by(TopicModel.order)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def create_topic(self, data: Dict[str, Any]) -> TopicModel:
        top = TopicModel(**data)
        self.session.add(top)
        await self.session.flush()
        return top

    # Concept Methods
    async def get_concepts_by_topic(self, topic_id: uuid.UUID) -> List[ConceptModel]:
        query = select(ConceptModel).where(ConceptModel.topic_id == topic_id, ConceptModel.deleted_at == None)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def get_concept_by_code(self, concept_code: str) -> Optional[ConceptModel]:
        query = (
            select(ConceptModel)
            .where(ConceptModel.concept_code == concept_code, ConceptModel.deleted_at == None)
            .options(
                selectinload(ConceptModel.objectives),
                selectinload(ConceptModel.misconceptions),
                selectinload(ConceptModel.resources),
                selectinload(ConceptModel.aliases),
            )
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def create_concept(self, data: Dict[str, Any]) -> ConceptModel:
        concept = ConceptModel(**data)
        self.session.add(concept)
        await self.session.flush()
        return concept

    # Relationships & Graph Methods
    async def create_relationship(
        self, source_id: uuid.UUID, target_id: uuid.UUID, rel_type: str = "Prerequisite"
    ) -> ConceptRelationshipModel:
        rel = ConceptRelationshipModel(
            source_concept_id=source_id,
            target_concept_id=target_id,
            relationship_type=rel_type,
        )
        self.session.add(rel)
        await self.session.flush()
        return rel

    async def get_concept_relationships(self, concept_id: uuid.UUID) -> List[ConceptRelationshipModel]:
        query = select(ConceptRelationshipModel).where(
            or_(
                ConceptRelationshipModel.source_concept_id == concept_id,
                ConceptRelationshipModel.target_concept_id == concept_id,
            )
        )
        result = await self.session.execute(query)
        return list(result.scalars().all())
