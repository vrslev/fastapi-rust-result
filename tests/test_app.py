import pytest
from fastapi.testclient import TestClient

from fastapi_rust_result import app


@pytest.fixture
def client():
    return TestClient(app)


def test_me_ok(client: TestClient):
    r = client.get("/me", params={"return_ok": True})
    assert r.status_code == 200
    assert r.json() == {"data": {"username": "lev"}}


def test_me_err(client: TestClient):
    r = client.get("/me", params={"return_ok": False})
    assert r.status_code == 200
    assert r.json() == {"error": {"username": "ivan"}}
