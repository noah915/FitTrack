# Sprint 2 — CI/CD Automation

Goal: Implement automated tests, CI pipeline, containerization, and automated deployment to Google Cloud Platform.

Deliverables:
- Automated test suite (`pytest`) that runs on every PR and push
- GitHub Actions workflows: `test.yml` and `deploy.yml`
- `Dockerfile` and `.dockerignore` for container builds
- Deployment to GCP Cloud Run (workflow template provided)
- Sprint review and retrospective notes in this document

Setup notes:
- To enable deployments you must configure the following GitHub secrets in the repository settings:
  - `GCP_PROJECT` — your GCP project id
  - `GCP_SA_KEY` — JSON service account key with permissions to push to Artifact Registry / Container Registry and deploy Cloud Run

How to run locally:

1. Create a virtual environment and install deps:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app:

```bash
python -m app.main
```

3. Run tests:

```bash
pytest -q
```

Retrospective (example):
- What went well: Tests created; CI runs on PRs; Dockerfile builds.
- What didn't go well: Automated deploy requires GitHub secrets and GCP service account; manual GCP setup required.
- Action items: Create a short runbook for creating the GCP service account and adding secrets.
