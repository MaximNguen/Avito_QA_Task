import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    def action(self, obj_id: str) -> None:
        self.delete_by_id(obj_id)

    @allure.step("Удаляем объявление по ID: {obj_id}")
    def delete_by_id(self, obj_id: str) -> None:
        self.response = requests.delete(f"{self.base_url}/api/2/item/{obj_id}")
        self.response_json = self.response.json()
        self.check_status_code(200)

    @allure.step("Подтверждаем, что объявление по ID {obj_id} удален")
    def verify_object_deleted(self, obj_id: str) -> None:
        self.response = requests.get(f"{self.base_url}/api/1/item/{obj_id}")
        self.check_status_code(404)