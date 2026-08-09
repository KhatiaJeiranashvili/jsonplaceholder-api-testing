import pytest
from api.posts_api import PostsAPI
from api.users_api import UsersAPI

@pytest.fixture
def posts_api():
    return PostsAPI()

@pytest.fixture
def users_api():
    return UsersAPI()