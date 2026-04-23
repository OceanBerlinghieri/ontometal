from abc import ABC, abstractmethod
from pandas import DataFrame

from etl.repository.resource.base_resource import BaseResource


class CountryRepository(ABC):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    @abstractmethod
    def get_countries(self, path, header=0) -> DataFrame:
        pass
