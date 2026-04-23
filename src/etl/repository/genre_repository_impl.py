from pandas import DataFrame

from etl.repository.genre_repository import GenreRepository
from etl.repository.resource.base_resource import BaseResource


class GenreRepositoryImpl(GenreRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_genres(self, path, header=0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)
