from abc import ABC, abstractmethod

from etl.entities.country import Country
from rdf_conversion.repository.resource.base_resource import BaseResource


class CountryRepository(ABC):
    def __init__(self, resource: BaseResource):
        pass

    @abstractmethod
    def get_countries(self, path: str) -> list[Country]:
        pass
