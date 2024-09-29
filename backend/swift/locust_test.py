# Atom: It's a script to test payload of the system.

from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_test(self):
        self.client.get("/")