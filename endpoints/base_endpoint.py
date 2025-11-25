from abc import ABC
import allure

class BaseEndpoint(ABC):
    def __init__(self, base_url: str = None):
        self.base_url = base_url or "https://qa-internship.avito.com"
        self.response = None
        self.response_json = None

    def action(self, *args, **kwargs):
        pass

    @allure.step("Проверяем статус код, что он {expected_code}")
    def check_status_code(self, expected_code: int):
        actual_code = self.response.status_code
        assert actual_code == expected_code, \
            f"Ожидали статус {expected_code}, получили {actual_code}. Ответ: {self.response.text}"