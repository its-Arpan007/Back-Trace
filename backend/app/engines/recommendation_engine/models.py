from dataclasses import dataclass


@dataclass
class RecommendationItem:
    item_id: str
    title: str
    target_concept_id: str
    priority: int = 1
