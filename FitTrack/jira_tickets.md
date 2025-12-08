# Jira Ticket Templates for Sprint 2 & 3

Copy these into Jira when creating issues.

-- Sprint 2: Add automated test suite
Summary: Add automated test suite for core app functionality
Description: Implement `pytest` tests for health endpoints and core logic. Ensure tests run locally and in CI.
Acceptance criteria:
- Tests present and passing locally
- Tests run in GitHub Actions on PRs

Subtasks:
- Write unit tests for `/api/health` and `/api/steps`
- Add integration/smoke tests
- Add instructions to README

-- Sprint 2: Add CI workflow
Summary: Add GitHub Actions workflow to run tests on PRs and pushes
Description: Create `/.github/workflows/test.yml` to run `pytest`.

-- Sprint 2: Containerize and Deploy
Summary: Add `Dockerfile` and deploy action for Cloud Run
Description: Add Dockerfile, push image to GCR, and deploy to Cloud Run via `deploy.yml`.

-- Sprint 3: Feature enhancement X
Summary: Implement feature X (replace with domain-specific feature)
Description: Design, implement, and test the enhancement. Update docs and demo.
