from locust import HttpUser, between, task
from loguru import logger
import json


class ModelUser(HttpUser):
    # Wait between 1 and 3 seconds between requrests
    wait_time = between(1, 3)

    def on_start(self):
        logger.info("Load your model here")

    @task
    def predict(self):
        logger.info("Sending POST requests!")
        essay = {
            "text": "This is a test essay used for performance testing with Locust."
        }
        self.client.post(
            "/predict",
            data=json.dumps(essay)
        )
        # logger.info("Sending GET requests!")
        # self.client.get(
        #     "/simple",
        # )
