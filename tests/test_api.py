import pytest
import allure

from endpoints.endpoint_factory import EndpointFactory
from utils.consts import Payloads

@pytest.fixture
def api_factory():
    factory = EndpointFactory()
    yield factory
    factory.clear_cache()

@pytest.fixture
def test_object_id(api_factory):
    create_object = api_factory.create_endpoint()
    object_id = create_object.new_object(Payloads.create_payload)
    yield object_id
    delete_object = api_factory.delete_endpoint()
    delete_object.delete_by_id(object_id)

