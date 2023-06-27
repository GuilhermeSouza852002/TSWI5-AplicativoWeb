from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def my_task(self):
        response = self.client.get('/my_endpoint')
        if response.status_code == 200:
            self.locust.events.request_success.fire(
                request_type="GET",
                name="/my_endpoint",
                response_time=response.elapsed.total_seconds() * 1000,
                response_length=len(response.content)
            )
        else:
            self.locust.events.request_failure.fire(
                request_type="GET",
                name="/my_endpoint",
                response_time=response.elapsed.total_seconds() * 1000,
                exception=response.raise_for_status()
            )
