import pandas as pd

from etl.repository.resource.base_resource import BaseResource


class CSVResource(BaseResource):
    def load(self, file_path: str, header: int = 0) -> pd.DataFrame:
        return pd.read_csv(file_path, header=header)

    def save(self, data: pd.DataFrame, file_path: str):
        data.to_csv(file_path, index=False)
