import requests
from api.logger import logger

class BaseAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def request(self, method, endpoint, **kwargs):
        url = f"{self.BASE_URL}{endpoint}"

        logger.info(f"{method} {url}")

        response = requests.request(
            method,
            url,
            **kwargs
        )

        logger.info(f"Status Code: {response.status_code}")

        return response

    def get(self, endpoint):
        return self.request("GET", endpoint)

    def post(self, endpoint, payload):
        return self.request("POST", endpoint, json=payload)

    def put(self, endpoint, payload):
        return self.request("PUT", endpoint, json=payload)

    def delete(self, endpoint):
        return self.request("DELETE", endpoint)
    