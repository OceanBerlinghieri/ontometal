from abc import ABC, abstractmethod

from etl.entities.release import Release
from rdf_conversion.repository.resource.base_resource import BaseResource


class ReleaseRepository(ABC):
    def __init__(self, resource: BaseResource):
        pass

    @abstractmethod
    def get_releases(self, path: str) -> list[Release]:
        pass
