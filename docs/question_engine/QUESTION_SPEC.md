# BACKTRACE Question Intelligence Specification

## 1. Educational Intelligence Object Model
Questions in BACKTRACE are not static items. Every question is a structured Educational Intelligence Object:

```
Question (Entity)
├── Primary & Secondary Concept DAG Nodes
├── Prerequisite Concepts Map
├── Bloom Taxonomy Level (remember, understand, apply, analyze, evaluate, create)
├── Misconception Library Map (Codes, Clues, Severity)
├── Root Cause Weight Matrix (Concept Gap, Prerequisite Gap, Calculation, Logic)
├── Multi-Level Hint Sequence (Levels 1-4)
├── Test Cases & Evaluation Rubrics
└── Analytics Statistics (Accuracy, Drop Off Rate, Misconception Frequency)
```

---

## 2. Supported Question Types (14 Total)
1. `MCQ`
2. `Multiple Select`
3. `True False`
4. `Fill in the Blank`
5. `Short Answer`
6. `Long Answer`
7. `Code`
8. `Code Output`
9. `Drag and Drop`
10. `Matching`
11. `Numerical`
12. `Diagram Based`
13. `Assertion Reason`
14. `Case Study`
