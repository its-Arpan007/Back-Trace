# Student Learning Model (SLM) Specification

## 1. Digital Twin Cognitive Architecture
The Student Learning Model (SLM) serves as the permanent digital twin of every student's evolving cognitive state in BACKTRACE:

```
Student Learning Model (SLM Digital Twin)
├── Concept Knowledge State (Bayesian P_know, P_transit, P_slip, P_guess)
├── Ebbinghaus Retention & Decay Curves (R = e^(-t/S))
├── Learning Velocity Metrics (Speed, Acquisition Rate, Recovery Speed)
├── Concept Progression Timelines (Day 1 -> Day 4 -> Day 14)
├── Mastery Predictions & Risk Analysis (Readiness, Est Time to Mastery)
└── Goal & Streak Tracking (Target Mastery %, Streak Days)
```

---

## 2. Performance SLA
- Incremental Mastery Update SLA: **<100 ms**
- Prediction Generation SLA: **<300 ms**
- Asynchronous Event Bus Integration: Listens to `DiagnosisCompleted` & `LearningSessionCompleted`, publishes `MasteryUpdated`, `KnowledgeStateChanged`, `StudentModelUpdated`, `ReviewRequired`.
