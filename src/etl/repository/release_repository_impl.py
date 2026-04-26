from pandas import DataFrame

from etl.entities.release import Release
from etl.repository.release_repository import ReleaseRepository
from etl.repository.resource.base_resource import BaseResource


class ReleaseRepositoryImpl(ReleaseRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_releases(self, path: str, header: int =0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)
    
    def write_releases(self, releases: DataFrame, path: str):
        self.resource.save(data=releases, file_path=path)