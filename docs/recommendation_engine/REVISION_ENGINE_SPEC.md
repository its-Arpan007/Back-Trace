# Spaced Revision & Decay Recovery Specification

## 1. Revision Scheduler
Calculates review dates based on Ebbinghaus Knowledge Decay retention thresholds:

$$\text{Review Urgency} = \begin{cases} \text{Critical} & \text{if } R < 0.70 \\ \text{High} & \text{if } R < 0.80 \\ \text{Medium} & \text{otherwise} \end{cases}$$
