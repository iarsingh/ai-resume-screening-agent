from fastapi.testclient import TestClient
from screen.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'screen this resume', **{'payload': {'skills': ['python', 'gcp'], 'required': ['python', 'kubernetes']}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["missing"] == ["kubernetes"]
    refused = client.post("/agent/run", json={"goal": 'email the candidate a reject'}).json()
    assert refused["refused"] is True
