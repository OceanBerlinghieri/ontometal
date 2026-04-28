import pandas as pd

from rdf_conversion.repository.resource.base_resource import BaseResource


class CSVResource(BaseResource):
    def load(self, file_path: str, header: int = 0) -> pd.DataFrame:
        return pd.read_csv(file_path, header=header, low_memory=False)

    def save(self, data, file_path: str) -> None:
        raise NotImplementedError("CSVResource does not support save")
