import requests
import allure
from typing import Dict, Any

from endpoints.base_endpoint import BaseEndpoint

class GetStatistic(BaseEndpoint):
    def action(self, obj_id: str):
        return self.get_object_by_id(obj_id)

    def action_wrong(self, obj_id: str):
        return self.get_object_by_id_wrong(obj_id)

    @allure.step("Получаем статистику объявления по ID: {obj_id}")
    def get_object_by_id(self, obj_id: str) -> Dict[str, Any]:
        self.response = requests.get(f"{self.base_url}/api/1/statistic/{obj_id}")
        self.response_json = self.response.json()
        self.check_status_code(200)
        return self.response_json

    @allure.step("Не получаем статистику объявления по ID: {obj_id}")
    def get_object_by_id_wrong(self, obj_id: str) -> Dict[str, Any]:
        self.response = requests.get(f"{self.base_url}/api/1/statistic/{obj_id}")
        self.response_json = self.response.json()
        self.check_status_code(400)
        return self.response_json