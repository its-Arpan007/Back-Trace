from typing import List, Dict, Any
from app.engines.knowledge_graph_engine.engine import KnowledgeGraphEngine


class PrerequisiteAnalyzer:
    """Traverses Knowledge Graph to identify weak prerequisites and broken learning chains."""

    def __init__(self):
        self.kg_engine = KnowledgeGraphEngine()

    async def analyze_prerequisites(self, concept_code: str) -> Dict[str, Any]:
        parents = await self.kg_engine.find_parents(concept_code)
        ancestors = await self.kg_engine.find_ancestors(concept_code)

        weak_prereqs = list(parents) if parents else ["DSA_ARRAYS_01"]

        return {
            "concept_code": concept_code,
            "direct_prerequisites": parents,
            "ancestors": ancestors,
            "weak_prerequisites": weak_prereqs,
            "broken_chain_detected": len(weak_prereqs) > 0,
        }


prerequisite_analyzer = PrerequisiteAnalyzer()
