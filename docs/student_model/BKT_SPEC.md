# Bayesian Knowledge Tracing (BKT) Specification

## 1. Mathematical Formulation
Bayesian Knowledge Tracing (BKT) models student knowledge acquisition across discrete problem attempts.

### Posterior Probability $P(L_t \mid \text{Obs})$
Given prior knowledge probability $P(L_t)$:

If response is correct:
$$P(L_t \mid \text{Correct}) = \frac{P(L_t) \cdot (1 - P(S))}{P(L_t) \cdot (1 - P(S)) + (1 - P(L_t)) \cdot P(G)}$$

If response is incorrect:
$$P(L_t \mid \text{Incorrect}) = \frac{P(L_t) \cdot P(S)}{P(L_t) \cdot P(S) + (1 - P(L_t)) \cdot (1 - P(G))}$$

### Transition Step
$$P(L_{t+1}) = P(L_t \mid \text{Obs}) + \left(1 - P(L_t \mid \text{Obs})\right) \cdot P(T)$$

Where:
- $P(L_0) = 0.20$ (Initial Knowledge)
- $P(T) = 0.15$ (Learning Probability)
- $P(S) = 0.10$ (Slip Probability)
- $P(G) = 0.20$ (Guess Probability)
