# BACKTRACE Multi-Cloud Deployment Guide

## 1. Supported Clouds
BACKTRACE supports seamless deployment across:
- **Google Cloud Platform (GCP)**: Google Kubernetes Engine (GKE) + Cloud SQL PostgreSQL.
- **Amazon Web Services (AWS)**: Elastic Kubernetes Service (EKS) + Amazon RDS PostgreSQL.
- **Microsoft Azure**: Azure Kubernetes Service (AKS) + Azure Database for PostgreSQL.
- **DigitalOcean & Self-Hosted**: Kubernetes Cluster via k3s / kubeadm.

---

## 2. Fast-Start Deployment
```bash
# 1. Start Local Production Stack
docker-compose -f docker-compose.prod.yml up -d --build

# 2. Deploy to Kubernetes
kubectl apply -f deploy/k8s/
```
