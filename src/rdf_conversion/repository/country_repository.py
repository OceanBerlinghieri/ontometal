from abc import ABC, abstractmethod
from pandas import DataFrame

from rdf_conversion.repository.resource.base_resource import BaseResource


class CountryRepository(ABC):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    @abstractmethod
    def get_countries(self, path: str) -> DataFrame:
        pass
