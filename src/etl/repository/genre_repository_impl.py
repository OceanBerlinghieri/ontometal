from pandas import DataFrame

from etl.entities.genre import Genre
from etl.repository.genre_repository import GenreRepository
from etl.repository.resource.base_resource import BaseResource


class GenreRepositoryImpl(GenreRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_genres(self, path: str, header: int = 0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)

    def get_band_genres(self, path: str, header: int = 0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)[["Genre"]]

    def get_label_specializations(self, path: str, header: int = 0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)[
            ["Specialization"]
        ].rename(columns={"Specialization": "Genre"})
    
    def write_genres(self, genres: DataFrame, path: str) -> None:
        self.resource.save(data=genres, file_path=path)