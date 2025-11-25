import pytest
import allure

from endpoints.endpoint_factory import EndpointFactory
from utils.consts import Payloads

@allure.feature("Сервис от Авито")
@allure.story("API тестирование ручек (4 на данный момент) - Негативные тест-кейсы")
class TestCRUDNegative:

    @classmethod
    def setup_class(cls):
        print("\n========= Начало выполнения негативных тестов ==========")

    @classmethod
    def teardown_class(cls):
        print("\n========= Конец выполнения негативных тестов ==========\n")

    @pytest.fixture
    def api_factory(self):
        factory = EndpointFactory()
        yield factory
        factory.clear_cache()

    @pytest.fixture
    def test_object_id(self, api_factory):
        create_object = api_factory.create_endpoint()
        object_id = create_object.new_object(Payloads.create_payload)
        yield object_id
        delete_object = api_factory.delete_endpoint()
        delete_object.delete_by_id(object_id)

    @allure.title("Не можем создать новое объявление - негативный тест-кейс №1")
    def test_create_object_negative(self, api_factory):
        with allure.step("Создаем объявление с помощью Page Object"):
            new_object = api_factory.create_endpoint()
            new_object.new_object(Payloads.create_payload_wrong)

        with allure.step("Проверяем статус кода"):
            new_object.check_status_code(400)

    @allure.title("Не получаем созданное объявление - негативный тест-кейс №2")
    def test_get_object(self, api_factory, test_object_id):
        with allure.step("Получаем айди объявления"):
            get_object = api_factory.get_endpoint()
            get_object.get_object_by_id(test_object_id)

        with allure.step("Достоверимся, что получили объявление"):
            get_object.check_status_code(200)