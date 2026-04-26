from abc import ABC, abstractmethod
from pandas import DataFrame

from etl.repository.resource.base_resource import BaseResource


class CountryRepository(ABC):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    @abstractmethod
    def get_countries(self, path: str, header: int = 0) -> DataFrame:
        pass

    @abstractmethod
    def get_band_countries(self, path: str, header: int = 0) -> DataFrame:
        pass

    @abstractmethod
    def get_label_countries(self, path: str, header: int = 0) -> DataFrame:
        pass

    @abstractmethod
    def write_countries(self, countries: DataFrame, path: str) -> None:
        pass
