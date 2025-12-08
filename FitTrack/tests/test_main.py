import json

from app.main import app


def test_health():
    client = app.test_client()
    resp = client.get("/api/health")
    assert resp.status_code == 200
    body = resp.get_json()
    assert body["status"] == "ok"


def test_index():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.get_json()
    assert "Welcome to FitTrack" in body.get("message", "")


def test_record_steps_success():
    client = app.test_client()
    resp = client.post("/api/steps", data=json.dumps({"steps": 5000}), content_type="application/json")
    assert resp.status_code == 201
    body = resp.get_json()
    assert body["recorded"] == 5000


def test_record_steps_bad_request():
    client = app.test_client()
    resp = client.post("/api/steps", data=json.dumps({}), content_type="application/json")
    assert resp.status_code == 400
