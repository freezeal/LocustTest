import json
import random
from locust import HttpUser, task, between, SequentialTaskSet

class TestUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        data = {
            "username": "admin","password": "1234"
        }
        self.client.post("/login_api", json.dumps(data), headers={"Content-Type": "application/json"})

    def on_stop(self):
        self.client.post("/logout_api")

    @task
    def Home(self):
        self.client.get("/home")

    @task
    def Calculator(self):
        num1 = random.randint(1, 2000)
        num2 = random.randint(1, 2000)
        operator = random.choice(["add", "subtract", "multiply", "divide"])
        params = {
            "num1": num1, "num2": num2
        }
        self.client.get(f"/calculator_api/{operator}", params=params)
        #self.client.get("/calculator_api/subtract", params=params)
        #self.client.get("/calculator_api/multiply", params=params)
        #self.client.get("/calculator_api/divide", params=params)

    @task
    def HistoryView(self):
        self.client.get("/history_view")

    @task
    def HistoryAPI(self):
        self.client.get("/history_api")