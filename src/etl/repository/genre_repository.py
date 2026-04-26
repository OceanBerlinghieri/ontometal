from abc import ABC, abstractmethod
from pandas import DataFrame

from etl.repository.resource.base_resource import BaseResource


class GenreRepository(ABC):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    # TODO: Add get_genres method to retrieve all genres from both bands and labels without 
    # duplicates and null values. This can be done through a conf reading file that specifies
    # the paths to the band and label datasets.
    @abstractmethod
    def get_band_genres(self, path: str, header: int = 0) -> DataFrame:
        pass

    @abstractmethod
    def get_label_specializations(self, path: str, header: int = 0) -> DataFrame:
        pass

    @abstractmethod
    def write_genres(self, genres: DataFrame, path: str) -> None:
        pass
