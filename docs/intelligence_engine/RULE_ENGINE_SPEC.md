# BACKTRACE Rule Engine Specification

## 1. Primary Source of Truth
Diagnostic determinations rely on the deterministic `RuleEngine`. Generative AI models are strictly prohibited from overriding rule evaluations.

---

## 2. Rule Types
- **Concept Rules (`R_CONCEPT_*`)**: Triggers when specific conceptual formulas are violated.
- **Prerequisite Rules (`R_PREREQ_*`)**: Triggers when upstream graph prerequisites are unmastered.
- **Misconception Rules (`R_MIS_*`)**: Triggers when choice/code matches known misconception codes.
- **Time & Pattern Rules (`R_TIME_*`, `R_PATTERN_*`)**: Triggers on rushing, guessing, or time pressure.
