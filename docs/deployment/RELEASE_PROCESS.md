# Semantic Versioning & Release Manual

## 1. Release Strategy
- Semantic Versioning (`v1.0.0`, `v1.1.0`).
- Blue/Green and Canary deployment strategies via Nginx Ingress annotations.
- Zero-downtime rolling updates (`maxSurge: 25%`, `maxUnavailable: 0`).
