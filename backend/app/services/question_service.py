import uuid
from typing import Optional, List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.question import QuestionModel
from app.repositories.question_repository import QuestionRepository
from app.engines.question_engine.engine import QuestionEngine
from app.engines.question_engine.importer import question_importer
from app.engines.question_engine.exporter import question_exporter
from app.engines.question_engine.validator import question_validator
from app.engines.question_engine.search import question_search_service
from app.schemas.question import QuestionCreateRequest, PracticeSetRequest


class QuestionService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = QuestionRepository(db)
        self.q_engine = QuestionEngine()

    async def get_all_questions(self) -> List[QuestionModel]:
        return await self.repo.get_all_questions()

    async def get_question_by_id(self, question_id: uuid.UUID) -> Optional[QuestionModel]:
        return await self.repo.get_question_by_id(question_id)

    async def create_question(self, req: QuestionCreateRequest) -> QuestionModel:
        data = req.model_dump()
        data["subject_id"] = uuid.UUID(data["subject_id"]) if data.get("subject_id") else None
        data["chapter_id"] = uuid.UUID(data["chapter_id"]) if data.get("chapter_id") else None
        data["topic_id"] = uuid.UUID(data["topic_id"]) if data.get("topic_id") else None
        data["primary_concept_id"] = uuid.UUID(data["primary_concept_id"]) if data.get("primary_concept_id") else None

        # Exclude nested lists for relational creation
        tags = data.pop("tags", [])
        hints = data.pop("hints", [])
        test_cases = data.pop("test_cases", [])
        misconceptions = data.pop("misconceptions", [])
        root_causes = data.pop("root_causes", [])
        data.pop("secondary_concept_ids", None)
        data.pop("prerequisite_concept_ids", None)

        return await self.repo.create_question(data)

    async def generate_practice_set(self, req: PracticeSetRequest) -> Dict[str, Any]:
        return await self.q_engine.generate_practice_set(
            concept_codes=req.concept_codes,
            difficulty=req.difficulty,
            count=req.question_count,
        )

    async def import_question_package(self, questions_list: List[Dict[str, Any]]) -> Dict[str, Any]:
        return question_importer.import_question_package(questions_list)
