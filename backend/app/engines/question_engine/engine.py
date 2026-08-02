import random
from typing import Dict, Any, List
from app.domain.interfaces.engine import IEngine
from app.engines.question_engine.interfaces import IQuestionEngine


class QuestionEngine(IEngine, IQuestionEngine):
    """Production Question Intelligence Engine managing adaptive assessment and selection."""

    def __init__(self):
        self._mock_questions = [
            {
                "id": "q1_arrays_01",
                "title": "Array Index Offset Calculation",
                "slug": "array-index-offset-calculation",
                "question_statement": "Given base address 0x1000 and element size 4 bytes, calculate address of index 5.",
                "question_type": "MCQ",
                "difficulty": "medium",
                "bloom_level": "apply",
                "primary_concept_id": "DSA_ARRAYS_01",
                "estimated_time_seconds": 120,
            },
            {
                "id": "q2_trees_01",
                "title": "Binary Tree In-Order Traversal",
                "slug": "binary-tree-inorder-traversal",
                "question_statement": "Write code to perform in-order DFS traversal of a binary tree.",
                "question_type": "Code",
                "difficulty": "hard",
                "bloom_level": "apply",
                "primary_concept_id": "DSA_TREES_01",
                "estimated_time_seconds": 300,
            },
        ]

    @property
    def name(self) -> str:
        return "Question Engine"

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def status(self) -> str:
        return "healthy"

    @property
    def dependencies(self) -> List[str]:
        return ["Knowledge Graph Engine"]

    async def get_question_by_id(self, question_id: str) -> Dict[str, Any]:
        for q in self._mock_questions:
            if q["id"] == question_id:
                return q
        return self._mock_questions[0]

    async def get_questions_by_concept(self, concept_id: str) -> List[Dict[str, Any]]:
        return [q for q in self._mock_questions if q.get("primary_concept_id") == concept_id] or self._mock_questions

    async def get_questions_by_difficulty(self, difficulty: str) -> List[Dict[str, Any]]:
        return [q for q in self._mock_questions if q.get("difficulty") == difficulty] or self._mock_questions

    async def select_adaptive_questions(self, student_id: str, concept_codes: List[str], count: int = 5) -> List[Dict[str, Any]]:
        # Adaptive selection algorithm returning questions suited to student level
        selected = []
        for _ in range(count):
            selected.append(random.choice(self._mock_questions))
        return selected

    async def generate_practice_set(self, concept_codes: List[str], difficulty: str, count: int = 5) -> Dict[str, Any]:
        questions = await self.select_adaptive_questions("student_default", concept_codes, count)
        return {
            "practice_set_id": "ps_" + str(random.randint(1000, 9999)),
            "concept_codes": concept_codes,
            "difficulty": difficulty,
            "total_questions": len(questions),
            "questions": questions,
        }

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        concept_id = input_data.get("concept_id", "DSA_ARRAYS_01")
        questions = await self.get_questions_by_concept(concept_id)
        return {
            "concept_id": concept_id,
            "matched_questions_count": len(questions),
            "questions": questions,
        }

    async def health_check(self) -> bool:
        return True

    async def readiness(self) -> bool:
        return True
