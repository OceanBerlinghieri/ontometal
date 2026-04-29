
from etl.entities.release import Release
from rdf_conversion.repository.band_repository import BandRepository
from rdf_conversion.repository.resource.base_resource import BaseResource


class BandRepositoryImpl(BandRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_band_mapping(self, path: str) -> dict[int, tuple[str, int]]:
        df = self.resource.load(file_path=path)
        return {row["bandId"]: (row["bandName"], row["bandId"]) for _, row in df.iterrows()}
