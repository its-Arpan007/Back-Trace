from typing import Dict, Any, List, Set
from app.domain.interfaces.engine import IEngine
from app.engines.knowledge_graph_engine.interfaces import IKnowledgeGraphEngine
from app.engines.knowledge_graph_engine.learning_path import learning_path_engine


class KnowledgeGraphEngine(IEngine, IKnowledgeGraphEngine):
    """Production Directed Acyclic Graph (DAG) Knowledge Graph Engine."""

    def __init__(self):
        # Default graph dependency structure (source -> targets)
        self.adj_map: Dict[str, List[str]] = {
            "DSA_ARRAYS_01": ["DSA_TREES_01", "DSA_HASH_01"],
            "DSA_TREES_01": ["DSA_GRAPH_01"],
            "DSA_HASH_01": ["DSA_GRAPH_01"],
            "DSA_GRAPH_01": [],
        }

    @property
    def name(self) -> str:
        return "Knowledge Graph Engine"

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def status(self) -> str:
        return "healthy"

    @property
    def dependencies(self) -> List[str]:
        return []

    async def get_concept_prerequisites(self, concept_id: str) -> List[str]:
        # Return direct prerequisites for node
        prereqs = []
        for parent, children in self.adj_map.items():
            if concept_id in children:
                prereqs.append(parent)
        return prereqs

    async def find_parents(self, concept_id: str) -> List[str]:
        return await self.get_concept_prerequisites(concept_id)

    async def find_children(self, concept_id: str) -> List[str]:
        return self.adj_map.get(concept_id, [])

    async def find_ancestors(self, concept_id: str) -> List[str]:
        ancestors: Set[str] = set()

        def dfs(curr: str):
            parents = [p for p, children in self.adj_map.items() if curr in children]
            for p in parents:
                if p not in ancestors:
                    ancestors.add(p)
                    dfs(p)

        dfs(concept_id)
        return list(ancestors)

    async def find_descendants(self, concept_id: str) -> List[str]:
        descendants: Set[str] = set()

        def dfs(curr: str):
            children = self.adj_map.get(curr, [])
            for c in children:
                if c not in descendants:
                    descendants.add(c)
                    dfs(c)

        dfs(concept_id)
        return list(descendants)

    async def topological_sort(self) -> List[str]:
        visited: Set[str] = set()
        stack: List[str] = []

        def dfs(node: str):
            visited.add(node)
            for child in self.adj_map.get(node, []):
                if child not in visited:
                    dfs(child)
            stack.append(node)

        all_nodes = set(self.adj_map.keys())
        for children in self.adj_map.values():
            all_nodes.update(children)

        for node in all_nodes:
            if node not in visited:
                dfs(node)

        return stack[::-1]

    async def detect_cycles(self) -> List[List[str]]:
        visited: Set[str] = set()
        rec_stack: Set[str] = set()
        cycles: List[List[str]] = []

        def dfs(node: str, path: List[str]):
            visited.add(node)
            rec_stack.add(node)
            path.append(node)

            for neighbor in self.adj_map.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, path.copy())
                elif neighbor in rec_stack:
                    idx = path.index(neighbor)
                    cycles.append(path[idx:] + [neighbor])

            rec_stack.remove(node)

        for node in self.adj_map.keys():
            if node not in visited:
                dfs(node, [])

        return cycles

    async def find_learning_path(self, target_concept: str) -> List[str]:
        ancestors = await self.find_ancestors(target_concept)
        # Topological order of ancestors + target
        full_subgraph = ancestors + [target_concept]
        top_order = await self.topological_sort()
        return [c for c in top_order if c in full_subgraph]

    async def find_weak_chain(self, student_id: str) -> List[str]:
        return ["DSA_ARRAYS_01"]

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        concept_id = input_data.get("concept_id", "DSA_GRAPH_01")
        parents = await self.find_parents(concept_id)
        children = await self.find_children(concept_id)
        ancestors = await self.find_ancestors(concept_id)
        path = await self.find_learning_path(concept_id)

        return {
            "concept_id": concept_id,
            "parents": parents,
            "children": children,
            "ancestors": ancestors,
            "learning_path": path,
        }

    async def health_check(self) -> bool:
        return True

    async def readiness(self) -> bool:
        return True
