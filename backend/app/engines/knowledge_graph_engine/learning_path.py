from typing import List, Dict, Any, Set


class LearningPathEngine:
    """Computes optimal, remediation, and revision learning paths across concept DAG nodes."""

    def compute_optimal_path(self, target_concept: str, concept_prereqs_map: Dict[str, List[str]]) -> List[str]:
        path: List[str] = []
        visited: Set[str] = set()

        def dfs(node: str):
            if node in visited:
                return
            visited.add(node)
            for prereq in concept_prereqs_map.get(node, []):
                dfs(prereq)
            path.append(node)

        dfs(target_concept)
        return path

    def compute_remediation_path(self, failed_concept: str, missing_prereqs: List[str]) -> List[str]:
        remediation_sequence = list(missing_prereqs)
        if failed_concept not in remediation_sequence:
            remediation_sequence.append(failed_concept)
        return remediation_sequence

    def compute_revision_path(self, mastered_concepts: List[str], target_concept: str) -> List[str]:
        return [c for c in mastered_concepts if c != target_concept] + [target_concept]


learning_path_engine = LearningPathEngine()
