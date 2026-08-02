from typing import Dict, Any, List


class ResourceMatchingEngine:
    """Matches educational learning resources (videos, articles, visualizers) to student gaps."""

    def match_resources(
        self,
        concept_code: str,
        misconception_code: str = None,
    ) -> List[Dict[str, Any]]:
        resources = [
            {
                "resource_id": "res_video_01",
                "resource_type": "video",
                "title": "Interactive Visualizer: Array Memory Stride & Pointer Offsets",
                "url": "https://backtrace.edu/lessons/arrays-stride-visualizer",
                "difficulty": "medium",
                "est_minutes": 10,
                "match_score": 0.96,
                "reasoning": f"Directly targets offset calculation misconception for {concept_code}.",
            },
            {
                "resource_id": "res_article_01",
                "resource_type": "article",
                "title": "Deep Dive: Memory Contiguity & Index Offset Math",
                "url": "https://backtrace.edu/articles/memory-contiguity",
                "difficulty": "easy",
                "est_minutes": 5,
                "match_score": 0.88,
                "reasoning": f"Explains fundamental prerequisites for {concept_code}.",
            },
        ]
        return resources


resource_matcher = ResourceMatchingEngine()
