# Kubernetes Deployment & Scaling Manual

## 1. Deployment Execution
- `kubectl apply -f deploy/k8s/namespace.yaml`
- `kubectl apply -f deploy/k8s/configmap.yaml`
- `kubectl apply -f deploy/k8s/secrets.yaml`
- `kubectl apply -f deploy/k8s/`
- `kubectl rollout status deployment/backtrace-backend -n backtrace-prod`
