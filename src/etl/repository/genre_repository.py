from abc import ABC, abstractmethod
from pandas import DataFrame

from etl.repository.resource.base_resource import BaseResource


class GenreRepository(ABC):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    # TODO: Add get_genres method to retrieve all genres from both bands and labels without duplicates and null values
    @abstractmethod
    def get_band_genres(self, path, header=0) -> DataFrame:
        pass

    @abstractmethod
    def get_label_specializations(self, path, header=0) -> DataFrame:
        pass
