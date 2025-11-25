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
        with allure.step("Создаем объявление с невалидными данными с помощью Page Object"):
            new_object = api_factory.create_endpoint()
            new_object.action_wrong(Payloads.create_payload_wrong)

        with allure.step("Проверяем статус кода"):
            new_object.check_status_code(400)

    @allure.title("Не получаем созданное объявление - негативный тест-кейс №2")
    def test_get_object_wrong(self, api_factory, test_object_id):
        with allure.step("Указываем пустой айди объявления"):
            get_object = api_factory.get_endpoint()
            get_object.action_wrong("")

        with allure.step("Достоверимся, что получили ошибку при попытке получить несуществующее объявление"):
            get_object.check_status_code(404)

    @allure.title("Не получаем объявления определенного продавца - негативный тест-кейс №3")
    def test_get_list_object_wrong(self, api_factory):
        with allure.step("Введем некорректный айди продавца"):
            get_object = api_factory.get_all_endpoint()
            get_object.action_wrong("testIdInvalidYeahYeah")

        with allure.step("Достоверимся, что получили Not Found"):
            get_object.check_status_code(400)

    @allure.title("Не получаем статистику объявление - негативный тест-кейс №4")
    def test_get_stats_object_wrong(self, api_factory, test_object_id):
        with allure.step("Указываем неверный"):
            get_object = api_factory.get_stat_endpoint()
            get_object.action_wrong("BububububInvalidData(((")

        with allure.step("Достоверимся, что получили ошибку Not Found"):
            get_object.check_status_code(400)

    @allure.title("Пробуем удалить несуществующий/невалидный тип ID объявление - негативный тест-кейс №5")
    def test_delete_object_wrong(self, api_factory):
        with allure.step("Указываем неверный"):
            delete_object = api_factory.delete_endpoint()
            delete_object.action("CantDelete?(((")

        with allure.step("Достоверимся, что получили ошибку Not Found"):
            delete_object.check_status_code(400)