from abc import ABC, abstractmethod

from etl.entities.label import Label
from rdf_conversion.repository.resource.base_resource import BaseResource


class LabelRepository(ABC):
    def __init__(self, resource: BaseResource):
        pass
    @abstractmethod
    def get_labels(self, path: str) -> list[Label]:
        pass
