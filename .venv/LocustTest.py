from locust import HttpUser, task, between
import json

class TestUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def LoginAPI(self):
        data = {
            "username": "admin"
            ,"password": "1234"
        }
        self.client.post("/login_api", json.dumps(data), headers={"Content-Type": "application/json"})