from abc import ABC, abstractmethod

from etl.entities.release import Release
from rdf_conversion.repository.resource.base_resource import BaseResource


class BandRepository(ABC):
    def __init__(self, resource: BaseResource):
        pass

    @abstractmethod
    def get_band_mapping(self, path: str) -> dict[int, tuple[str, int]]:
        pass
