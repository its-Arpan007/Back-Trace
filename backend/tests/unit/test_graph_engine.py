import pytest
from app.engines.knowledge_graph_engine.engine import KnowledgeGraphEngine
from app.engines.knowledge_graph_engine.learning_path import learning_path_engine
from app.engines.knowledge_graph_engine.exporter import curriculum_exporter


@pytest.mark.asyncio
async def test_dag_traversals():
    engine = KnowledgeGraphEngine()
    parents = await engine.find_parents("DSA_GRAPH_01")
    assert "DSA_TREES_01" in parents or "DSA_HASH_01" in parents

    children = await engine.find_children("DSA_ARRAYS_01")
    assert "DSA_TREES_01" in children

    ancestors = await engine.find_ancestors("DSA_GRAPH_01")
    assert "DSA_ARRAYS_01" in ancestors

    descendants = await engine.find_descendants("DSA_ARRAYS_01")
    assert "DSA_GRAPH_01" in descendants


@pytest.mark.asyncio
async def test_topological_sort_and_cycles():
    engine = KnowledgeGraphEngine()
    top_sort = await engine.topological_sort()
    assert len(top_sort) >= 4
    cycles = await engine.detect_cycles()
    assert len(cycles) == 0


def test_learning_path_engine():
    m = {"C": ["B"], "B": ["A"], "A": []}
    path = learning_path_engine.compute_optimal_path("C", m)
    assert path == ["A", "B", "C"]


def test_exporter():
    res = curriculum_exporter.export_concept_graph("dsa", [], [])
    assert res["domain"] == "dsa"
    assert res["graph_version"] == "1.0.0"
