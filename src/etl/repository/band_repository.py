from abc import ABC, abstractmethod

from pandas import DataFrame

from etl.repository.resource.base_resource import BaseResource


class BandRepository(ABC):
    def __init__(self, resource: BaseResource):
        pass

    @abstractmethod
    def get_bands(self, path, header=0) -> DataFrame:
        pass
