import pytest
import allure

from endpoints.endpoint_factory import EndpointFactory
from utils.consts import Payloads

@allure.feature("Сервис от Авито")
@allure.story("API тестирование ручек (4 на данный момент) - Позитивные тест-кейсы")
class TestCRUD:

    @classmethod
    def setup_class(cls):
        print("\n========= Начало выполнения позитивных тестов ==========")

    @classmethod
    def teardown_class(cls):
        print("\n========= Конец выполнения позитивных тестов ==========\n")

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
        with allure.step("Успешно удаляем объявление"):
            delete_object = api_factory.delete_endpoint()
            delete_object.action(object_id)
            delete_object.verify_object_deleted(object_id)

    @allure.title("Создаем новое объявление - позитивный тест-кейс №1.1")
    def test_create_object(self, api_factory):
        with allure.step("Создаем объявление с помощью Page Object"):
            new_object = api_factory.create_endpoint()
            new_object.action(Payloads.create_payload)

        with allure.step("Проверяем статус кода"):
            new_object.check_status_code(200)

    @allure.title("Получаем созданное объявление - позитивный тест-кейс №2")
    def test_get_object(self, api_factory, test_object_id):
        with allure.step("Получаем айди объявления"):
            get_object =  api_factory.get_endpoint()
            get_object.action(test_object_id)

        with allure.step("Достоверимся, что получили объявление"):
            get_object.check_status_code(200)

    @allure.title("Получаем объявления определенного продавца - позитивный тест-кейс №3")
    def test_get_list_object(self, api_factory):
        with allure.step("Получаем айди продавца"):
            get_object = api_factory.get_all_endpoint()
            get_object.action(1)

        with allure.step("Достоверимся, что получили список объявлений"):
            get_object.check_status_code(200)

    @allure.title("Получаем статистику объявление - позитивный тест-кейс №4")
    def test_get_stats_object(self, api_factory, test_object_id):
        with allure.step("Получаем айди объявления"):
            get_object = api_factory.get_stat_endpoint()
            get_object.action(test_object_id)

        with allure.step("Достоверимся, что получили объявление"):
            get_object.check_status_code(200)