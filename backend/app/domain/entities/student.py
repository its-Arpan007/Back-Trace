from dataclasses import dataclass, field
from typing import List
from app.domain.entities.base import Entity


@dataclass
class StudentEntity(Entity):
    email: str = ""
    full_name: str = ""
    is_active: bool = True
    role: str = "student"
    enrolled_courses: List[str] = field(default_factory=list)

    def deactivate(self) -> None:
        self.is_active = False

    def activate(self) -> None:
        self.is_active = True
