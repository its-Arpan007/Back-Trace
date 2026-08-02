# BACKTRACE Mastery Engine Specification

## 1. Incremental Update Engine
The `MasteryEngine` updates concept mastery after every diagnostic event:

- **Target Update Latency**: $<100$ ms
- **Plateau Detection**: Triggered when 3 consecutive attempts yield static mastery ($\Delta < 0.02$).
- **Regression Detection**: Triggered when diagnostic detects a prerequisite or misconception gap.
- **Recovery Progress**: Tracks mastery restoration after targeted remediation.
