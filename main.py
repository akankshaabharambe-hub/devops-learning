from flask import Flask, jsonify, request

app = Flask(__name__)

TOOLS = {
    "github": "Source control, pull requests, and CI/CD workflow trigger",
    "github_actions": "Runs automated tests, quality checks, and image build steps",
    "sonarqube": "Scans code for bugs, code smells, coverage, and vulnerabilities",
    "docker": "Packages the app and dependencies into a portable container image",
    "harbor_artifactory": "Stores built container images and other build artifacts",
    "argocd": "Syncs deployment configuration from Git to Kubernetes using GitOps",
    "kubernetes": "Runs and manages application containers through pods, deployments, and services",
    "rancher": "Provides a dashboard to manage Kubernetes clusters and workloads",
    "vault": "Manages secrets such as API keys, database passwords, and tokens"
}

@app.route("/")
def home():
    return jsonify({
        "project": "Platform Delivery Demo",
        "message": "A small demo showing how modern DevOps/platform tools connect together.",
        "flow": [
            "GitHub", "GitHub Actions", "SonarQube", "Docker Build",
            "Harbor/Artifactory", "ArgoCD", "Kubernetes", "Rancher", "Vault"
        ]
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/tools")
def tools():
    return jsonify(TOOLS)

@app.route("/analyze", methods=["POST"])
def analyze_repo():
    data = request.get_json(silent=True) or {}
    repo_name = data.get("repo", "sample-service")
    return jsonify({
        "repo": repo_name,
        "summary": "Simulated platform readiness analysis",
        "checks": {
            "github_repo": "present",
            "ci_pipeline": "recommended: GitHub Actions",
            "quality_gate": "recommended: SonarQube scan before merge/deploy",
            "containerization": "recommended: Dockerfile present",
            "artifact_storage": "recommended: push image to Harbor or Artifactory",
            "deployment": "recommended: ArgoCD syncs Kubernetes manifests",
            "secrets": "recommended: use Vault, never hardcode secrets"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
