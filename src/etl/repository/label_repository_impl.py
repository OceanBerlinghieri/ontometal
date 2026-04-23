from pandas import DataFrame

from etl.repository.label_repository import LabelRepository
from etl.repository.resource.base_resource import BaseResource


class LabelRepositoryImpl(LabelRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_labels(self, path, header=0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)
