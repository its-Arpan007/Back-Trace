import uuid
from typing import Optional, List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.curriculum import SubjectModel, ChapterModel, TopicModel, ConceptModel
from app.repositories.curriculum_repository import CurriculumRepository
from app.engines.knowledge_graph_engine.engine import KnowledgeGraphEngine
from app.engines.knowledge_graph_engine.importer import curriculum_importer
from app.engines.knowledge_graph_engine.exporter import curriculum_exporter
from app.engines.knowledge_graph_engine.search import curriculum_search_service
from app.schemas.curriculum import (
    SubjectSchema, SubjectCreateRequest,
    ChapterSchema, ChapterCreateRequest,
    TopicSchema, TopicCreateRequest,
    ConceptSchema, ConceptCreateRequest,
)


class CurriculumService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = CurriculumRepository(db)
        self.kg_engine = KnowledgeGraphEngine()

    # Subject Business Methods
    async def get_all_subjects(self) -> List[SubjectModel]:
        return await self.repo.get_all_subjects()

    async def get_subject(self, subject_id: uuid.UUID) -> Optional[SubjectModel]:
        return await self.repo.get_subject_by_id(subject_id)

    async def create_subject(self, req: SubjectCreateRequest) -> SubjectModel:
        return await self.repo.create_subject(req.model_dump())

    # Chapter Business Methods
    async def get_chapters_by_subject(self, subject_id: uuid.UUID) -> List[ChapterModel]:
        return await self.repo.get_chapters_by_subject(subject_id)

    async def create_chapter(self, req: ChapterCreateRequest) -> ChapterModel:
        data = req.model_dump()
        data["subject_id"] = uuid.UUID(data["subject_id"])
        return await self.repo.create_chapter(data)

    # Topic Business Methods
    async def get_topics_by_chapter(self, chapter_id: uuid.UUID) -> List[TopicModel]:
        return await self.repo.get_topics_by_chapter(chapter_id)

    async def create_topic(self, req: TopicCreateRequest) -> TopicModel:
        data = req.model_dump()
        data["chapter_id"] = uuid.UUID(data["chapter_id"])
        return await self.repo.create_topic(data)

    # Concept Business Methods
    async def get_concepts_by_topic(self, topic_id: uuid.UUID) -> List[ConceptModel]:
        return await self.repo.get_concepts_by_topic(topic_id)

    async def get_concept_by_code(self, concept_code: str) -> Optional[ConceptModel]:
        return await self.repo.get_concept_by_code(concept_code)

    async def create_concept(self, req: ConceptCreateRequest) -> ConceptModel:
        data = req.model_dump()
        data["topic_id"] = uuid.UUID(data["topic_id"])
        # Exclude nested lists from model instantiation
        objectives = data.pop("objectives", [])
        misconceptions = data.pop("misconceptions", [])
        resources = data.pop("resources", [])
        return await self.repo.create_concept(data)

    # Graph Intelligence Methods
    async def get_full_graph(self) -> Dict[str, Any]:
        top_sort = await self.kg_engine.topological_sort()
        return {
            "domain": "dsa",
            "graph_version": "1.0.0",
            "topological_order": top_sort,
            "adj_map": self.kg_engine.adj_map,
        }

    async def get_concept_dependencies(self, concept_code: str) -> Dict[str, Any]:
        parents = await self.kg_engine.find_parents(concept_code)
        children = await self.kg_engine.find_children(concept_code)
        ancestors = await self.kg_engine.find_ancestors(concept_code)
        descendants = await self.kg_engine.find_descendants(concept_code)
        path = await self.kg_engine.find_learning_path(concept_code)

        return {
            "concept_code": concept_code,
            "parents": parents,
            "children": children,
            "ancestors": ancestors,
            "descendants": descendants,
            "optimal_learning_path": path,
        }

    async def import_curriculum_package(
        self, domain: str, graph_json: Dict[str, Any], concepts_json: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        return curriculum_importer.import_curriculum_package(
            domain=domain,
            graph_data=graph_json,
            concepts_list=concepts_json,
        )
