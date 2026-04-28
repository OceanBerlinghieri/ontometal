from etl.entities.genre import Genre
from rdf_conversion.repository.genres_repository import GenreRepository
from rdf_conversion.repository.resource.base_resource import BaseResource


class GenreRepositoryImpl(GenreRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_genres(self, path: str) -> list[Genre]:
        df = self.resource.load(file_path=path)
        return [Genre(id=row["id"], name=row["name"]) for _, row in df.iterrows()]

