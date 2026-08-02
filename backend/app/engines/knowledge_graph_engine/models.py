from dataclasses import dataclass, field
from typing import List


@dataclass
class KnowledgeNode:
    node_id: str
    title: str
    domain: str
    prerequisites: List[str] = field(default_factory=list)
