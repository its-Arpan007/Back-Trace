# Ebbinghaus Knowledge Decay Specification

## 1. Retention Curve Formula
$$R = e^{-\frac{t}{S}}$$

Where:
- $R$: Predicted retention score $[0.0, 1.0]$
- $t$: Days elapsed since last practice attempt
- $S$: Memory strength parameter derived from half-life $S = \frac{T_{1/2}}{\ln(2)}$
- $T_{1/2}$: Half-life in days (Default: 14 days)
