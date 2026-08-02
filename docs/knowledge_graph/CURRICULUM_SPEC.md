# BACKTRACE Curriculum Hierarchy & Importer Specification

## 1. Domain Package Structure
Domains (`dsa`, `math`, `physics`, `chemistry`, `biology`) are defined as self-contained JSON packages:

- `graph.json`: Edge definitions and version metadata.
- `concepts.json`: Concept attributes, Bloom levels, estimated time, and mastery thresholds.
- `questions.json`: Diagnostic question metadata and misconception mapping.
- `resources.json`: Video, article, and interactive lesson links.

---

## 2. Validation Constraints
The `CurriculumValidator` strictly checks for:
- Zero directed cycles ($G$ is a valid DAG).
- No orphan edges (source/target concept codes must exist).
- Unique concept codes across domain namespace.
- Valid Bloom Taxonomy levels (`remember`, `understand`, `apply`, `analyze`, `evaluate`, `create`).
