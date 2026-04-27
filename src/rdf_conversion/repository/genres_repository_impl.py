from abc import ABC, abstractmethod
from pandas import DataFrame

from rdf_conversion.repository.resource.base_resource import BaseResource


class GenreRepository(ABC):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_genres(self, path: str) -> DataFrame:
        return self.resource.load(file_path=path)

