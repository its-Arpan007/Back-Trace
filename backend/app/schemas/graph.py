from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class GraphNodeDTO(BaseModel):
    id: str
    concept_code: str
    title: str
    domain: str
    difficulty: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class GraphEdgeDTO(BaseModel):
    source: str
    target: str
    relationship_type: str = "Prerequisite"
    weight: float = 1.0


class KnowledgeGraphDTO(BaseModel):
    domain: str
    graph_version: str = "1.0.0"
    nodes: List[GraphNodeDTO] = Field(default_factory=list)
    edges: List[GraphEdgeDTO] = Field(default_factory=list)


class LearningPathDTO(BaseModel):
    path_id: Optional[str] = None
    title: str
    domain: str
    path_type: str = "optimal" # optimal, remediation, revision
    concept_sequence: List[str] = Field(default_factory=list)


class ValidationReportDTO(BaseModel):
    valid: bool
    domain: str
    graph_version: str
    total_concepts: int
    total_edges: int
    errors: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)


class GraphImportRequest(BaseModel):
    domain: str
    graph_json: Dict[str, Any]
    concepts_json: List[Dict[str, Any]]
    questions_json: Optional[List[Dict[str, Any]]] = None
    resources_json: Optional[List[Dict[str, Any]]] = None
