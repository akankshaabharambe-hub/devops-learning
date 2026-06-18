# Platform Delivery — Siemens Stack Learning Project

Built this project to understand the platform engineering ecosystem before joining Siemens.
It maps the full software delivery lifecycle and shows where each tool fits.

## The pipeline

```
Developer
    ↓
GitHub Enterprise       ← source control, pull requests, code review
    ↓
GitHub Actions          ← CI/CD: runs tests, scans, builds automatically on every push
    ↓
SonarQube               ← code quality gate: bugs, security issues, coverage
    ↓
Docker Build            ← packages the app and its dependencies into a container
    ↓
Harbor / Artifactory    ← stores the built container image and other artifacts
    ↓
ArgoCD (GitOps)         ← watches Git, syncs changes to Kubernetes automatically
    ↓
Kubernetes              ← runs and scales the containers (pods, deployments, services)
    ↓
Rancher                 ← management dashboard for Kubernetes clusters
    ↓
Application running     ← live, scaled, self-healing

Vault ──────────────────→ injects secrets securely into Kubernetes at runtime
```

## What this repo contains

- `main.py` — Flask app with endpoints simulating a platform readiness analysis
- `test_app.py` — unit tests
- `.github/workflows/ci.yaml` — GitHub Actions CI pipeline (checkout → test → SonarQube placeholder → Docker build)
- `Dockerfile` — containerizes the Flask app
- `k8s/` — Kubernetes Deployment and Service manifests
- `argocd/application.yaml` — ArgoCD application config showing GitOps sync
- `sonar-project.properties` — SonarQube project config

## The AI agent idea

The `/analyze` endpoint simulates what an AI agent could do across this pipeline:

- Read a GitHub repository and check for required files (Dockerfile, CI workflow, k8s manifests)
- Check SonarQube quality results before allowing deployment
- Verify artifacts exist in Harbor or Artifactory
- Confirm ArgoCD sync status with Kubernetes
- Report overall deployment readiness in one place

A real agent would connect these tools together and surface problems automatically,
reducing manual coordination across the delivery lifecycle.

## What each tool does

| Tool | Purpose |
|------|---------|
| GitHub Enterprise | Stores code, manages branches and pull requests |
| GitHub Actions | Runs tests and builds automatically on every push |
| SonarQube | Checks code quality, security, and test coverage |
| Docker | Packages the app into a portable container |
| Harbor / Artifactory | Stores built images and artifacts |
| ArgoCD | Deploys automatically when Git changes (GitOps) |
| Kubernetes | Runs, scales, and self-heals containers |
| Rancher | UI dashboard for managing Kubernetes clusters |
| Vault | Stores secrets — passwords, tokens, API keys |

## Run locally

```bash
pip install -r requirements.txt
python main.py
```

Endpoints: `GET /` · `GET /health` · `GET /tools` · `POST /analyze`

## Run with Docker

```bash
docker build -t platform-delivery-demo .
docker run -p 5000:5000 platform-delivery-demo
```

## Note

The goal was to understand how these tools connect before Day 1, not to replace a senior platform engineer.
