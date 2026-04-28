from abc import ABC, abstractmethod

from etl.entities.genre import Genre
from rdf_conversion.repository.resource.base_resource import BaseResource


class GenreRepository(ABC):
    def __init__(self, resource: BaseResource):
        pass
    @abstractmethod
    def get_genres(self, path: str) -> list[Genre]:
        pass
