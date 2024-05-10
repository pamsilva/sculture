import pytest

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_latest_posts():
    response = client.get("/posts/")

    assert response.status_code == 200
    assert response.json() == []


def test_invalid_post():
    response = client.post("/posts/", json={"title": "test", "content": "test"})

    assert response.status_code == 422
