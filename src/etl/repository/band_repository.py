from abc import ABC, abstractmethod

from pandas import DataFrame

from etl.repository.resource.base_resource import BaseResource


class BandRepository(ABC):
    def __init__(self, resource: BaseResource):
        pass

    @abstractmethod
    def get_bands(self, path: str, header: int = 0) -> DataFrame:
        pass

    @abstractmethod
    def write_bands(self, bands: DataFrame, path: str) -> None:
        pass