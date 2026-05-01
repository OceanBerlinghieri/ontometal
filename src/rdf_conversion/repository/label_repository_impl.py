import pandas as pd

from etl.entities.label import Label
from rdf_conversion.repository.label_repository import LabelRepository
from rdf_conversion.repository.resource.base_resource import BaseResource


class LabelRepositoryImpl(LabelRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_labels(self, path: str) -> list[Label]:
        df = self.resource.load(file_path=path)
        df["hasCountry"] = pd.to_numeric(df["hasCountry"], errors="coerce").astype("Int64")
        return [Label(
            labelId=row["labelId"], 
            labelName=row["labelName"],
            status=row["status"],
            websiteUrl=row["websiteUrl"],
            producer=[int(x) for x in str(row["producer"]).split(",") if x.strip().isdigit()],
            hasSpecialization=[x.strip() for x in str(row["hasSpecialization"]).split(",") if x.strip()],
            hasCountry=row["hasCountry"])
            for _, row in df.iterrows()]
    
    def get_label_mapping(self, path: str) -> dict[int, tuple[str, int]]:
        df = self.resource.load(file_path=path)
        return {row["labelId"]: (row["labelName"], row["labelId"]) for _, row in df.iterrows()}
