from abc import ABC, abstractmethod

from pandas import DataFrame

from etl.repository.release_repository import ReleaseRepository
from etl.repository.resource.base_resource import BaseResource


class ReleaseRepositoryImpl(ReleaseRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_releases(self, path, header=0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)