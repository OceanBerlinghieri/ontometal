from pandas import DataFrame

from etl.repository.band_repository import BandRepository
from etl.repository.resource.base_resource import BaseResource


class BandRepositoryImpl(BandRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_bands(self, path, header=0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)
