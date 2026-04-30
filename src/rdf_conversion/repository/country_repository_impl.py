from etl.entities.country import Country
from rdf_conversion.repository.country_repository import CountryRepository
from rdf_conversion.repository.resource.base_resource import BaseResource


class CountryRepositoryImpl(CountryRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_countries(self, path: str) -> list[Country]:
        df = self.resource.load(file_path=path)
        return [Country(id=row["id"], name=row["name"]) for _, row in df.iterrows()]

    def get_country_mapping(self, path: str) -> dict[int, tuple[str, int]]:
        df = self.resource.load(file_path=path)
        return {row["id"]: (row["name"], row["id"]) for _, row in df.iterrows()}