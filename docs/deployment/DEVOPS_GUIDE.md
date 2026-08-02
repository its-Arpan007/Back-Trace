# DevOps & Infrastructure as Code Guide

## 1. GitOps & Twelve-Factor Principles
- Infrastructure stored declaratively in `deploy/k8s/`.
- Environment configuration via Kubernetes `ConfigMap` and `Secret`.
- Automated container builds via GitHub Actions CI/CD workflows (`.github/workflows/ci.yml` & `deploy.yml`).
