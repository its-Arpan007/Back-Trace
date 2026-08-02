from typing import List, Dict, Any


class QuestionSearchService:
    """Fuzzy search and filter for questions by title, concept, difficulty, bloom level, tags, or question type."""

    def search_questions(self, query: str, questions_pool: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        q = query.strip().lower()
        if not q:
            return questions_pool

        results = []
        for question in questions_pool:
            title = question.get("title", "").lower()
            slug = question.get("slug", "").lower()
            stmt = question.get("question_statement", "").lower()
            tags = [t.lower() for t in question.get("tags", [])]
            q_type = question.get("question_type", "").lower()

            if q in title or q in slug or q in stmt or q in q_type or any(q in t for t in tags):
                results.append(question)

        return results


question_search_service = QuestionSearchService()
