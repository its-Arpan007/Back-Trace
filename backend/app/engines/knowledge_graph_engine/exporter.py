import json
from typing import Dict, Any, List


class CurriculumExporter:
    """Exports subjects, chapters, concepts, and knowledge graphs into JSON format."""

    def export_to_json(self, data: Dict[str, Any]) -> str:
        return json.dumps(data, indent=2)

    def export_concept_graph(self, domain: str, nodes: List[Dict[str, Any]], edges: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            "graph_version": "1.0.0",
            "domain": domain,
            "status": "active",
            "nodes": nodes,
            "edges": edges,
        }


curriculum_exporter = CurriculumExporter()
