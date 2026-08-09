from api.base_api import BaseAPI

class PostsAPI(BaseAPI):

    def get_post(self, post_id):
        return self.get(f"/posts/{post_id}")

    def create_post(self, payload):
        return self.post("/posts",payload)

    def update_post(self, post_id, payload):
        return self.put(f"/posts/{post_id}", payload)

    def delete_post(self, post_id):
        return self.delete(f"/posts/{post_id}")