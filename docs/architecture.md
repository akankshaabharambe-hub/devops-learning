# Architecture Flow

```text
Developer
  ↓
GitHub Repository
  ↓
GitHub Actions CI Pipeline
  ↓
Unit Tests + SonarQube Quality Scan
  ↓
Docker Image Build
  ↓
Harbor / Artifactory Artifact Storage
  ↓
ArgoCD GitOps Sync
  ↓
Kubernetes Deployment + Service
  ↓
Rancher for Cluster Visibility
  ↓
Vault for Secrets Management
```

## What this demo proves

This demo is intentionally small. It is not a production deployment. The goal is to show understanding of how platform engineering tools connect in a software delivery lifecycle.

## Tool mapping

| Tool | Role in the workflow |
|---|---|
| GitHub | Stores code and triggers CI/CD |
| GitHub Actions | Runs tests, quality checks, and image build |
| SonarQube | Performs static code analysis and quality gates |
| Docker | Packages the app into a container image |
| Harbor / Artifactory | Stores images and build artifacts |
| ArgoCD | Deploys Kubernetes manifests from Git |
| Kubernetes | Runs and manages containers |
| Rancher | Provides Kubernetes cluster visibility and management |
| Vault | Stores secrets securely |
