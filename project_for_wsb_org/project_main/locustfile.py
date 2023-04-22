from locust import HttpUser, between, task


class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_form(self):
        self.client.get("/")

    @task(3)  # give more weight to this task
    def submit_form(self):
        payload = {
            "name": "John Smith"
        }
        self.client.post("/hello", data=payload)
