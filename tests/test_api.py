import pytest
import random

from fastapi.testclient import TestClient
from main import app
from sculture.data.db import engine
from sculture.data.schemas import Base

client = TestClient(app)

    
def test_latest_posts():
    response = client.get("/posts/")

    assert response.status_code == 200
    assert response.json() == []


def test_invalid_post():
    response = client.post("/posts/", json={"title": "test", "content": "test"})

    assert response.status_code == 422



def test_create_user():
    rand_api_key = str(random.randint(0, 1000000))
    response = client.post(
        "/users/", json={
            "name": "test",
            # TODO: avoid this by cleaning the db at each test run
            "apiKey": rand_api_key
        })
    assert response.status_code == 200
    data = response.json()

    assert data["apiKey"] == rand_api_key


            
    
