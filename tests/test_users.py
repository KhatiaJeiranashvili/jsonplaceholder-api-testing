def test_get_single_user(users_api):
    user_id = 1
    response = users_api.get_user(user_id)

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == user_id
    assert body["name"]
    assert body["email"]