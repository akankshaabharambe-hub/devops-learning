# Platform Delivery Demo

A small demo project to understand how GitHub, GitHub Actions, SonarQube, Docker, Harbor/Artifactory, ArgoCD, Kubernetes, Rancher, and Vault fit together in a modern software delivery lifecycle.

## What the app does

This is a simple Flask service with three endpoints:

- `GET /` — shows the overall delivery flow
- `GET /health` — health check endpoint
- `GET /tools` — explains each platform tool
- `POST /analyze` — simulates a platform readiness analysis for a repository

## Run locally

```bash
pip install -r requirements.txt
python -m app.main
```

Open:

```bash
http://localhost:5000
http://localhost:5000/health
http://localhost:5000/tools
```

## Run tests

```bash
pytest
```

## Run with Docker

```bash
docker build -t platform-delivery-demo .
docker run -p 5000:5000 platform-delivery-demo
```

## CI/CD workflow

The GitHub Actions workflow in `.github/workflows/ci.yml` performs:

1. Code checkout
2. Python setup
3. Dependency installation
4. Unit tests
5. Placeholder SonarQube scan
6. Docker image build
7. Placeholder push to Harbor/Artifactory

## Kubernetes and GitOps

The `k8s/` folder contains sample Kubernetes `Deployment` and `Service` manifests.

The `argocd/application.yaml` file shows how ArgoCD could sync the `k8s/` folder into a Kubernetes cluster.

## Vault note

The Kubernetes deployment references a secret value. In a real enterprise setup, this should come from Vault or an approved secrets-management integration, not from source code.

## Main learning outcome

This project is not meant to be production-ready. It is a learning demo showing how the tools connect:

```text
GitHub → GitHub Actions → SonarQube → Docker → Harbor/Artifactory → ArgoCD → Kubernetes → Rancher
                                            ↑
                                          Vault
```
