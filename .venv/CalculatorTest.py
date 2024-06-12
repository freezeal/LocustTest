from locust import HttpUser, task, between, SequentialTaskSet
import json
import random

class TestUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        data = {
            "username": "admin","password": "1234"
        }
        self.client.post("/login_api", json.dumps(data), headers={"Content-Type": "application/json"})

    def on_stop(self):
        self.client.post("/logout_api")

    #홈 화면 이동
    @task
    def Home(self):
        self.client.get("/home")

    #사칙 연산 시도
    @task
    def Calculator(self):
        num1 = random.randint(1, 2000)
        num2 = random.randint(1, 2000)
        operator = random.choice(["add", "subtract", "multiply", "divide"])
        params = {
            "num1": num1, "num2": num2
        }
        self.client.get(f"/calculator_api/{operator}", params=params)

    #히스토리 화면 이동
    @task
    def HistoryView(self):
        self.client.get("/history_view")

    #히스토리 API 호출
    @task
    def HistoryAPI(self):
        self.client.get("/history_api")