from typing import List, Dict, Any, Set, Tuple


class CurriculumValidator:
    """Validator performing static graph integrity, cycle detection, and reference checks."""

    def validate_graph(self, graph_data: Dict[str, Any], concepts_list: List[Dict[str, Any]]) -> Dict[str, Any]:
        errors: List[str] = []
        warnings: List[str] = []

        # 1. Concept IDs and Duplicate Check
        concept_ids: Set[str] = set()
        for concept in concepts_list:
            cid = concept.get("id", "")
            if not cid:
                errors.append("Found concept missing required 'id' field")
            elif cid in concept_ids:
                errors.append(f"Duplicate concept ID found: '{cid}'")
            else:
                concept_ids.add(cid)

        # 2. Graph Nodes vs Concepts Match
        nodes = set(graph_data.get("nodes", []))
        missing_nodes = concept_ids - nodes
        if missing_nodes:
            warnings.append(f"Concepts not declared in graph nodes list: {missing_nodes}")

        # 3. Edges & Broken References Check
        adj: Dict[str, List[str]] = {cid: [] for cid in concept_ids}
        edges = graph_data.get("edges", [])

        for edge in edges:
            src = edge.get("source", "")
            tgt = edge.get("target", "")

            if src not in concept_ids:
                errors.append(f"Broken edge source reference: '{src}' does not exist in concepts")
            if tgt not in concept_ids:
                errors.append(f"Broken edge target reference: '{tgt}' does not exist in concepts")

            if src in concept_ids and tgt in concept_ids:
                adj[src].append(tgt)

        # 4. Cycle Detection (DFS)
        visited: Set[str] = set()
        rec_stack: Set[str] = set()
        cycles_found: List[List[str]] = []

        def dfs(node: str, path: List[str]) -> None:
            visited.add(node)
            rec_stack.add(node)
            path.append(node)

            for neighbor in adj.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, path.copy())
                elif neighbor in rec_stack:
                    cycle_start = path.index(neighbor)
                    cycles_found.append(path[cycle_start:] + [neighbor])

            rec_stack.remove(node)

        for cid in concept_ids:
            if cid not in visited:
                dfs(cid, [])

        if cycles_found:
            for cycle in cycles_found:
                errors.append(f"Cycle detected in prerequisite graph: {' -> '.join(cycle)}")

        is_valid = len(errors) == 0

        return {
            "valid": is_valid,
            "domain": graph_data.get("domain", "unknown"),
            "graph_version": graph_data.get("graph_version", "1.0.0"),
            "total_concepts": len(concept_ids),
            "total_edges": len(edges),
            "errors": errors,
            "warnings": warnings,
        }


curriculum_validator = CurriculumValidator()
