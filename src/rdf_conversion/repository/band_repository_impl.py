
import pandas as pd

from etl.entities.band import Band
from etl.entities.release import Release
from rdf_conversion.repository.band_repository import BandRepository
from rdf_conversion.repository.resource.base_resource import BaseResource


class BandRepositoryImpl(BandRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_bands(self, path: str) -> list[Band]:
        df = self.resource.load(file_path=path)
        df["hasCountry"] = pd.to_numeric(df["hasCountry"], errors="coerce").astype("Int64")
        return [Band(
            bandId=row["bandId"],
            bandName=row["bandName"],
            status=row["status"],
            metalArchiveUrl=row["metalArchiveUrl"],
            releases=[int(x) for x in str(row["releases"]).split(",") if x.strip().isdigit()],
            producedBy=row["producedBy"],
            hasGenre=[x.strip() for x in str(row["hasGenre"]).split(",") if x.strip()],
            hasCountry=row["hasCountry"])
            for _, row in df.iterrows()]
    
    def get_band_mapping(self, path: str) -> dict[int, tuple[str, int]]:
        df = self.resource.load(file_path=path)
        return {row["bandId"]: (row["bandName"], row["bandId"]) for _, row in df.iterrows()}
