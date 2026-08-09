import pytest

@pytest.mark.parametrize("post_id", [1, 5, 10, 25])
def test_get_single_post(posts_api, post_id):

    response = posts_api.get_post(post_id)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == post_id

def test_create_post(posts_api):

    payload = {
        "title": "My first API test",
        "body": "Testing POST request",
        "userId": 1
    }

    response = posts_api.create_post(payload)

    assert response.status_code == 201

    body = response.json()

    assert body["title"] == "My first API test"
    assert body["body"] == "Testing POST request"
    assert body["userId"] == 1   

def test_update_post(posts_api):

    payload = {
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1
    }

    response = posts_api.update_post(1, payload)

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["title"] == "Updated title"
    assert response_body["body"] == "Updated body"
    assert response_body["userId"] == 1

def test_delete_post(posts_api):
    response = posts_api.delete_post(1)

    assert response.status_code == 200

def test_get_non_existing_post(posts_api):  
    response = posts_api.get_post(99999)
    assert response.status_code == 404
    
