from abc import ABC, abstractmethod
import pandas as pd

from etl.repository.resource.base_resource import BaseResource


class GenreRepository(ABC):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    @abstractmethod
    def get_genres(self, path, header=0) -> pd.DataFrame:
        pass
