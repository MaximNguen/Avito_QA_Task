import requests
import allure
from typing import Any, Dict

from endpoints.base_endpoint import BaseEndpoint

class CreateObject(BaseEndpoint):
    def __init__(self, base_url: str = None):
        super().__init__(base_url)
        self.endpoint_url = f"{self.base_url}/api/1/item"

    def action(self, payload: Dict[str, Any]):
        return self.new_object(payload)

    def action_wrong(self, payload: Dict[str, Any]):
        return self.new_object_wrong(payload)

    @allure.step("Создаем объявление с данными")
    def new_object(self, payload: Dict[str, Any]) -> str:
        self.response = requests.post(f"{self.endpoint_url}", json=payload)
        self.response_json = self.response.json()
        return self.response_json["status"].split()[3]

    @allure.step("Создаем объявление с некорректными данными")
    def new_object_wrong(self, payload: Dict[str, Any]) -> None:
        self.response = requests.post(f"{self.endpoint_url}", json=payload)
        self.response_json = self.response.json()
        return self.response_json