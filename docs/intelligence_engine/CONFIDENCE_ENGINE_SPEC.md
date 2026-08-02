# BACKTRACE Confidence Engine Specification

## 1. Confidence Formula
The `ConfidenceEngine` computes a deterministic $0–100\%$ confidence score:

$$\text{Confidence} = \text{BaseRuleWeight} + \min(|E| \times 3.5, 15.0) + \min(P_{\text{graph}} \times 2.0, 10.0)$$

Where:
- $\text{BaseRuleWeight}$: Base rule confidence (e.g. $85\%$)
- $|E|$: Number of compiled evidence records
- $P_{\text{graph}}$: Number of matched prerequisite DAG nodes
- Capped at maximum $98.5\%$
