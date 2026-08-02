# SRE & Incident Response Runbook

## 1. Incident Response Procedures
- **High CPU / Memory**: Scaled automatically by HPA (`backend-hpa.yaml`). Manual override: `kubectl scale deployment backtrace-backend --replicas=10 -n backtrace-prod`.
- **Database Connection Failure**: Check PgBouncer connection pooler health; fallback to read replicas.
- **Rollback Procedure**: `kubectl rollout undo deployment/backtrace-backend -n backtrace-prod`.
