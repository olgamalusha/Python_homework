import requests

from config import BASE_URL, TOKEN


class YougileApi:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }

    def create_project(self, body, use_auth=True):
        headers = self.headers if use_auth else {
            "Content-Type": "application/json"
        }

        return requests.post(
            f"{self.base_url}/projects",
            json=body,
            headers=headers
        )

    def update_project(self, project_id, body):
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=body,
            headers=self.headers
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
