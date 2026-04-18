from locust import HttpUser, task, between


class PetStoreUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://petstore.swagger.io/v2"

    @task
    def get_pet_by_valid_id(self):
        self.client.get("/pet/1", name="GET /pet/{valid_id}")

    @task
    def get_pet_by_invalid_id(self):
        with self.client.get("/pet/999999999", catch_response=True, name="GET /pet/{invalid_id}") as response:
            if response.status_code == 404:
                response.success()  # expected
            else:
                response.failure("Unexpected response")

    @task
    def find_pets_by_status(self):
        self.client.get("/pet/findByStatus?status=available", name="GET /pet/findByStatus")