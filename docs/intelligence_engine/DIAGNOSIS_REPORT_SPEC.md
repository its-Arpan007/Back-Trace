# BACKTRACE Diagnosis Report Specification

## 1. DiagnosisReport Schema
```json
{
  "student_id": "UUID",
  "question_id": "UUID",
  "concept_code": "DSA_ARRAYS_01",
  "is_correct": false,
  "score": 0.0,
  "primary_root_cause": "Concept Gap",
  "secondary_root_causes": ["Logic Error"],
  "confidence_score": 91.5,
  "severity": "high",
  "evidence": [...],
  "detected_misconceptions": [...],
  "weak_prerequisites": ["DSA_ARRAYS_01"],
  "bloom_level": "apply",
  "mastery_impact": {"delta": -0.10},
  "recommended_actions": [...],
  "processing_time_ms": 142.0,
  "engine_versions": {...}
}
```
