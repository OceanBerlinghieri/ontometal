from pandas import DataFrame

from etl.entities.label import Label
from etl.repository.label_repository import LabelRepository
from etl.repository.resource.base_resource import BaseResource


class LabelRepositoryImpl(LabelRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_labels(self, path: str, header: int = 0) -> DataFrame:
        return self.resource.load(file_path=path, header=header)
    
    def write_labels(self, labels: DataFrame, path: str) -> None:
        self.resource.save(data=labels, file_path=path)
