import json
import logging
from typing import Dict, Any, List
from app.curriculum.validator import curriculum_validator

logger = logging.getLogger("backtrace.curriculum_importer")


class CurriculumImporter:
    """Automated validator and importer for curriculum domain data files."""

    def import_curriculum_package(
        self,
        domain: str,
        graph_data: Dict[str, Any],
        concepts_list: List[Dict[str, Any]],
        questions_list: List[Dict[str, Any]] = None,
        resources_list: List[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        # Validate graph & concepts
        report = curriculum_validator.validate_graph(graph_data, concepts_list)
        if not report["valid"]:
            logger.error(f"Failed curriculum import for domain '{domain}': {report['errors']}")
            raise ValueError(f"Curriculum validation failed for domain '{domain}': {report['errors']}")

        imported_concepts = len(concepts_list)
        imported_edges = len(graph_data.get("edges", []))
        imported_questions = len(questions_list or [])
        imported_resources = len(resources_list or [])

        logger.info(
            f"Successfully imported curriculum for domain '{domain}': "
            f"{imported_concepts} concepts, {imported_edges} edges, {imported_questions} questions"
        )

        return {
            "success": True,
            "domain": domain,
            "imported_concepts": imported_concepts,
            "imported_edges": imported_edges,
            "imported_questions": imported_questions,
            "imported_resources": imported_resources,
            "validation_report": report,
        }


curriculum_importer = CurriculumImporter()
