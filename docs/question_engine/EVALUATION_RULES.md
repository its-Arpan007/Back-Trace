# BACKTRACE Question Evaluation & Rubric Rules Specification

## 1. Evaluation Strategies
- **Exact Match**: Direct string or key comparison.
- **Rubric Evaluation**: Multi-criteria weighted scoring matrix.
- **Code Evaluation**: Automated test case execution with expected runtime (ms) and asymptotic complexity checks ($O(N)$).
- **Partial Credit**: Partial point assignment based on misconception clues triggered.

---

## 2. Root Cause Weighting Matrix
When a student submits an incorrect response:
1. `RuleEngine` matches option choice or code output to `misconception_code`.
2. `QuestionRootCauseModel` returns probability weights across:
   - `Concept Gap`
   - `Prerequisite Gap`
   - `Calculation Error`
   - `Logic Error`
3. Results populate `DiagnosisReport` for downstream remediation by the BACKTRACE Intelligence Engine.
