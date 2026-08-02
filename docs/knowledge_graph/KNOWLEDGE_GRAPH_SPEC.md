# BACKTRACE Knowledge Graph Engine Specification

## 1. Directed Acyclic Graph (DAG) Model
The BACKTRACE Knowledge Graph represents educational concepts as nodes and prerequisite dependencies as directed edges.

```
Subject -> Chapter -> Topic -> Concept (Node)
                              │
                    Prerequisite Edge
                              ▼
                        Concept (Target)
```

---

## 2. Supported Relationship Types
- `Prerequisite`: Direct prerequisite knowledge required before attempting target concept.
- `Depends On`: Soft functional dependency.
- `Related`: Lateral conceptual correlation across subdomains.
- `Extension`: Deepening or advanced specialization.
- `Alternative`: Equivalent conceptual path.
- `Review`: Foundational refresher recommendation.

---

## 3. Graph Operations & Algorithms
1. **Depth-First Search (DFS)**: Ancestor/Descendant traversal, Cycle detection.
2. **Breadth-First Search (BFS)**: Shortest prerequisite distance calculation.
3. **Topological Sorting (Kahn / DFS)**: Produces total ordering for optimal learning path generation.
4. **Weak Chain Discovery**: Identifies unmastered upstream prerequisite nodes causing diagnostic failures downstream.
