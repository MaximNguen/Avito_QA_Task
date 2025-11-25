import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    def action(self, obj_id: str) -> None:
        self.delete_by_id(obj_id)

    @allure.step("Удаляем объявление по ID: {obj_id}")
    def delete_by_id(self, obj_id: str) -> None:
        self.response = requests.delete(f"{self.base_url}/api/2/item/{obj_id}")
        if self.response.content:
            try:
                self.response_json = self.response.json()
            except:
                self.response_json = {}
        else:
            self.response_json = {}

    @allure.step("Подтверждаем, что объявление по ID {obj_id} удален")
    def verify_object_deleted(self, obj_id: str) -> None:
        self.response = requests.get(f"{self.base_url}/api/1/item/{obj_id}")
        self.check_status_code(404)