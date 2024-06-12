from locust import HttpUser, task, between, SequentialTaskSet
import json

class LoginScenario(SequentialTaskSet):
    #로그인 홈 화면 이동
    @task
    def LoginHome(self):
        self.client.get("/")

    #로그인 API로 로그인 시도
    @task
    def LoginAPI(self):
        data = {
            "username": "admin","password": "1234"
        }
        self.client.post("/login_api", json.dumps(data), headers={"Content-Type": "application/json"})

    #홈 화면 이동
    @task
    def Home(self):
        self.client.get("/home")

    #로그아웃 API로 로그아웃 시도
    @task
    def LogoutAPI(self):
        self.client.post("/logout_api")

class TestUser(HttpUser):
    wait_time = between(1, 3)
    tasks = [LoginScenario]