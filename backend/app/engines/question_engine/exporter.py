import json
from typing import Dict, Any, List


class QuestionExporter:
    """Exports questions to JSON, YAML, or CSV format."""

    def export_to_json(self, questions: List[Dict[str, Any]]) -> str:
        return json.dumps(questions, indent=2)

    def export_to_csv(self, questions: List[Dict[str, Any]]) -> str:
        lines = ["id,title,slug,question_type,difficulty,bloom_level,primary_concept_id"]
        for q in questions:
            lines.append(
                f'{q.get("id","")},{q.get("title","")},{q.get("slug","")},'
                f'{q.get("question_type","")},{q.get("difficulty","")},{q.get("bloom_level","")},'
                f'{q.get("primary_concept_id","")}'
            )
        return "\n".join(lines)


question_exporter = QuestionExporter()
