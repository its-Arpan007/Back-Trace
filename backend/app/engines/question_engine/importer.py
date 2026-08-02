import json
import logging
from typing import Dict, Any, List
from app.engines.question_engine.validator import question_validator

logger = logging.getLogger("backtrace.question_importer")


class QuestionImporter:
    """Imports question packages (questions.json, rubrics.json, test_cases.json, resources.json)."""

    def import_question_package(
        self,
        questions_list: List[Dict[str, Any]],
        rubrics_list: List[Dict[str, Any]] = None,
        test_cases_list: List[Dict[str, Any]] = None,
        resources_list: List[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        report = question_validator.validate_questions(questions_list)
        if not report["valid"]:
            logger.error(f"Question import failed: {report['errors']}")
            raise ValueError(f"Question validation failed: {report['errors']}")

        logger.info(f"Successfully imported {len(questions_list)} educational intelligence questions")

        return {
            "success": True,
            "imported_questions": len(questions_list),
            "imported_rubrics": len(rubrics_list or []),
            "imported_test_cases": len(test_cases_list or []),
            "imported_resources": len(resources_list or []),
            "validation_report": report,
        }


question_importer = QuestionImporter()
