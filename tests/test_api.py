import pytest
import random

from fastapi.testclient import TestClient
from main import app
from sculture.data.db import engine
from sculture.data.schemas import Base
from sculture.data.interface import update_post

client = TestClient(app)


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


def test_create_post():
    # TODO: there has to be a better way of setting up the test scenario
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

    new_post_response = client.post(
        "/posts/", json={
            "title": "test",
            "body": "test content"
        },
        headers={
            "apiKey": rand_api_key,
            "userId": str(data["userId"])
        })

    assert new_post_response.status_code == 200

    new_post_data = new_post_response.json()
    assert new_post_data["title"] == "test"


def test_feedback_post():
    # TODO: there has to be a better way of setting up the test scenario
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

    new_post_response = client.post(
        "/posts/", json={
            "title": "test",
            "body": "test content"
        },
        headers={
            "apiKey": rand_api_key,
            "userId": str(data["userId"])
        })

    assert new_post_response.status_code == 200

    new_post_data = new_post_response.json()
    assert new_post_data["title"] == "test"

    feedback_response = client.post(
        "/feedback/", json={
            "postId": new_post_data["postId"],
            "positive": False
        },
        headers={
            "apiKey": rand_api_key,
            "userId": str(data["userId"])
        })

    assert feedback_response.status_code == 200


def test_fetch_posts():
    # TODO: there has to be a  way of setting up the test scenario
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

    for _ in range(13):
        new_post_response = client.post(
            "/posts/", json={
                "title": "test",
                "body": "test content"
            },
            headers={
                "apiKey": rand_api_key,
                "userId": str(data["userId"])
            })

        assert new_post_response.status_code == 200

    new_post_data = new_post_response.json()
    update_post({**new_post_data, "active": False})
    
    list_posts_response = client.get("/posts/")
    assert list_posts_response.status_code == 200

    posts = list_posts_response.json()
    assert len(posts) == 10

    # not active posts don't show up even if they are the latest
    assert new_post_data["postId"] not in [post["postId"] for post in posts]
