from dataclasses import dataclass
from app.domain.entities.base import Entity


@dataclass
class MasteryEntity(Entity):
    student_id: str = ""
    concept_id: str = ""
    mastery_score: float = 0.0
    mastery_level: str = "novice"
    attempts_count: int = 0
    success_count: int = 0
