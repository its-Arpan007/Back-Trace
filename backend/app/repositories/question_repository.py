import uuid
from typing import Optional, List, Dict, Any
from sqlalchemy import select, update, delete, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.question import (
    QuestionModel,
    QuestionVersionModel,
    QuestionTagModel,
    QuestionHintModel,
    QuestionTestCaseModel,
    QuestionEvaluationRuleModel,
    QuestionConceptModel,
    QuestionMisconceptionModel,
    QuestionRootCauseModel,
    QuestionStatisticsModel,
)


class QuestionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_questions(self) -> List[QuestionModel]:
        query = (
            select(QuestionModel)
            .where(QuestionModel.deleted_at == None)
            .options(
                selectinload(QuestionModel.tags),
                selectinload(QuestionModel.hints),
                selectinload(QuestionModel.test_cases),
                selectinload(QuestionModel.misconceptions),
                selectinload(QuestionModel.root_causes),
                selectinload(QuestionModel.statistics),
            )
        )
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def get_question_by_id(self, question_id: uuid.UUID) -> Optional[QuestionModel]:
        query = (
            select(QuestionModel)
            .where(QuestionModel.id == question_id, QuestionModel.deleted_at == None)
            .options(
                selectinload(QuestionModel.tags),
                selectinload(QuestionModel.hints),
                selectinload(QuestionModel.test_cases),
                selectinload(QuestionModel.misconceptions),
                selectinload(QuestionModel.root_causes),
                selectinload(QuestionModel.statistics),
            )
        )
        result = await self.session.execute(query)
        return result.scalars().first()

    async def get_questions_by_concept(self, concept_id: uuid.UUID) -> List[QuestionModel]:
        query = (
            select(QuestionModel)
            .where(QuestionModel.primary_concept_id == concept_id, QuestionModel.deleted_at == None)
            .options(
                selectinload(QuestionModel.hints),
                selectinload(QuestionModel.misconceptions),
                selectinload(QuestionModel.root_causes),
            )
        )
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def get_questions_by_difficulty(self, difficulty: str) -> List[QuestionModel]:
        query = (
            select(QuestionModel)
            .where(QuestionModel.difficulty == difficulty, QuestionModel.deleted_at == None)
        )
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def create_question(self, data: Dict[str, Any]) -> QuestionModel:
        question = QuestionModel(**data)
        self.session.add(question)
        await self.session.flush()

        # Initialize statistics
        stats = QuestionStatisticsModel(question_id=question.id)
        self.session.add(stats)
        await self.session.flush()
        return question
