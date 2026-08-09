from api.base_api import BaseAPI


class UsersAPI(BaseAPI):

    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")