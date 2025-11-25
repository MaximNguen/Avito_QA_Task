from endpoints.create_object import CreateObject
from endpoints.get_object_by_id import GetObject
from endpoints.get_objects_by_id import GetObjects
from endpoints.get_statistics_by_id import GetStatistic
from endpoints.delete_object_by_id import DeleteObject

from typing import Type

class EndpointFactory:
    def __init__(self, base_url: str = None):
        self.base_url = base_url
        self._endpoints_cache = {}

    def _create_endpoint(self, endpoint: Type, endpoint_name: str):
        if endpoint not in self._endpoints_cache:
            if self.base_url:
                self._endpoints_cache[endpoint_name] = endpoint(self.base_url)
            else:
                self._endpoints_cache[endpoint_name] = endpoint()

        return self._endpoints_cache[endpoint_name]

    def create_endpoint(self) -> CreateObject:
        return self._create_endpoint(CreateObject, 'create')

    def get_endpoint(self) -> GetObject:
        return self._create_endpoint(GetObject, 'get')

    def get_all_endpoint(self) -> GetObjects:
        return self._create_endpoint(GetObjects, 'update')

    def get_stat_endpoint(self) -> GetStatistic:
        return self._create_endpoint(GetStatistic, 'get')

    def delete_endpoint(self) -> DeleteObject:
        return self._create_endpoint(DeleteObject, 'delete')

    def clear_cache(self):
        self._endpoints_cache.clear()