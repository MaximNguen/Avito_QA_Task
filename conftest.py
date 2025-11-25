import pytest
from utils.consts import Payloads
from endpoints.create_object import CreateObject
from endpoints.delete_object_by_id import DeleteObject
import allure

@pytest.fixture
def create_object():
    create_object = CreateObject()
    delete_object = DeleteObject()

    create_object.new_object(Payloads.create_payload)
    obj_id = create_object.response_json["id"]
    yield obj_id

    with allure.step(f"Cleanup: delete object {obj_id}"):
        try:
            delete_object.delete_by_id(obj_id)
        except Exception as e:
            print(f"Cleanup warning: {e}")