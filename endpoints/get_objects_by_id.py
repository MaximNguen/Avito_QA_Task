import requests
import allure
from typing import Dict, Any

from endpoints.base_endpoint import BaseEndpoint

class GetObjects(BaseEndpoint):
    def action(self, obj_id: int):
        return self.get_objects_by_id(obj_id)

    def action_wrong(self, obj_id: str):
        return self.get_objects_by_id_wrong(obj_id)

    @allure.step("Получаем объявления по ID продавца: {obj_id}")
    def get_objects_by_id(self, obj_id: int) -> Dict[str, Any]:
        self.response = requests.get(f"{self.base_url}/api/1/{obj_id}/item")
        self.response_json = self.response.json()
        self.check_status_code(200)
        return self.response_json

    @allure.step("Не получаем объявления по ID продавца: {obj_id}")
    def get_objects_by_id_wrong(self, obj_id: str) -> Dict[str, Any]:
        self.response = requests.get(f"{self.base_url}/api/1/{obj_id}/item")
        self.response_json = self.response.json()
        self.check_status_code()
        return self.response_json