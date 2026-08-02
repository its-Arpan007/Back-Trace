from dataclasses import dataclass


@dataclass
class MasteryScore:
    student_id: str
    concept_id: str
    score: float
    level: str
