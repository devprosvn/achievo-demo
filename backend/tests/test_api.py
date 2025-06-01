from fastapi.testclient import TestClient

from backend.main import app, init_db

client = TestClient(app)


def setup_module() -> None:
    init_db()


def test_register_and_login_student() -> None:
    resp = client.post(
        "/students/register",
        json={"name": "Alice", "email": "alice@example.com", "password": "pwd"},
    )
    assert resp.status_code == 201
    resp = client.post(
        "/students/login",
        json={"email": "alice@example.com", "password": "pwd"},
    )
    assert resp.status_code == 200
