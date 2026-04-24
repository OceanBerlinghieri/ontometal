from pandas import DataFrame

from etl.repository.country_repository import CountryRepository
from etl.repository.resource.base_resource import BaseResource


class CountryRepositoryImpl(CountryRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_countries(self, path, header=0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)

    def get_band_countries(self, path, header=0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)[["Country"]]

    def get_label_countries(self, path, header=0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)[["Country"]]
