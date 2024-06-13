from locust import HttpUser, task, between, SequentialTaskSet
import json
import random

class HistoryScenario(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        data = {
            "username": "admin","password": "1234"
        }
        self.client.post("/login_api", json.dumps(data), headers={"Content-Type": "application/json"})

    def on_stop(self):
        self.client.post("/logout_api")

    #사칙연산 계산하기를 진행하는데 가중치를 설정
    @task(10)
    def Calculator(self):
        num1 = random.randint(1, 2000)
        num2 = random.randint(1, 2000)
        operator = random.choice(["add", "subtract", "multiply", "divide"])
        params = {
            "num1": num1, "num2": num2
        }
        self.client.get(f"/calculator_api/{operator}", params=params)

    #히스토리 화면 이동
    @task(2)
    def HistoryView(self):
        self.client.get("/history_view")

    #히스토리 API 호출
    @task(2)
    def HistoryAPI(self):
        self.client.get("/history_api")

    #히스토리 삭제 api 호출
    @task(1)
    def HistoryDel(self):
        self.client.delete("/delete_history")