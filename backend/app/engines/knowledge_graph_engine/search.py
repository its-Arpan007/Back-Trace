from typing import List, Dict, Any


class CurriculumSearchService:
    """Fuzzy search and autocomplete for subjects, chapters, topics, concepts, and aliases."""

    def search_curriculum(self, query: str, concepts_pool: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        q = query.strip().lower()
        if not q:
            return []

        results = []
        for concept in concepts_pool:
            title = concept.get("title", "").lower()
            code = concept.get("concept_code", "").lower()
            description = concept.get("description", "").lower()
            aliases = [a.lower() for a in concept.get("aliases", [])]

            if q in title or q in code or q in description or any(q in a for a in aliases):
                results.append(concept)

        return results


curriculum_search_service = CurriculumSearchService()
