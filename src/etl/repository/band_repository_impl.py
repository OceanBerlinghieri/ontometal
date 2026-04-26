from pandas import DataFrame

from etl.entities.band import Band
from etl.repository.band_repository import BandRepository
from etl.repository.resource.base_resource import BaseResource


class BandRepositoryImpl(BandRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_bands(self, path: str, header: int = 0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)
    
    def write_bands(self, bands: DataFrame, path: str) -> None:
        self.resource.save(data=bands, file_path=path)