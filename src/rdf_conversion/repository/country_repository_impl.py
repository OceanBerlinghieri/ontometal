from pandas import DataFrame

from rdf_conversion.repository.country_repository import CountryRepository
from rdf_conversion.repository.resource.base_resource import BaseResource


class CountryRepositoryImpl(CountryRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_countries(self, path: str) -> DataFrame:
        return self.resource.load(file_path=path)
