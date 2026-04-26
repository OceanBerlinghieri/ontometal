from abc import ABC, abstractmethod

from pandas import DataFrame

from etl.repository.resource.base_resource import BaseResource


class LabelRepository(ABC):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    @abstractmethod
    def get_labels(self, path: str, header: int =0) -> DataFrame:
        pass

    @abstractmethod
    def write_labels(self, labels: DataFrame, path: str):
        pass
