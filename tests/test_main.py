import pytest

from app.main import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def test_health_endpoint_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"service": "secure-app", "status": "ok"}
    assert response.headers["X-Content-Type-Options"] == "nosniff"


def test_greet_uses_default_name(client):
    response = client.get("/greet")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, world!"}


def test_greet_accepts_valid_name(client):
    response = client.get("/greet?name=DevSecOps_Team-1")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, DevSecOps_Team-1!"}


def test_greet_rejects_invalid_name(client):
    response = client.get("/greet?name=../../etc/passwd")
    assert response.status_code == 400
    body = response.get_json()
    assert body["error"].startswith("name must start with a letter")
