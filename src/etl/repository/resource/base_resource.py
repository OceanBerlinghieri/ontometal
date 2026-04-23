from abc import ABC, abstractmethod
import pandas as pd


class BaseResource(ABC):
    @abstractmethod
    def load(self, file_path: str, header: int = 0) -> pd.DataFrame:
        pass

    @abstractmethod
    def save(self, data: pd.DataFrame, file_path: str) -> None:
        pass
