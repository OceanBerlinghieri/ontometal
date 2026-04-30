
from etl.entities.release import Release
from rdf_conversion.repository.release_repository import ReleaseRepository
from rdf_conversion.repository.resource.base_resource import BaseResource


class ReleaseRepositoryImpl(ReleaseRepository):
    def __init__(self, resource: BaseResource):
        self.resource = resource

    def get_releases(self, path: str) -> list[Release]:
        df = self.resource.load(file_path=path)
        return [Release(
            releaseId=row["releaseId"], 
            releaseTitle=row["releaseTitle"],
            releaseYear=row["releaseYear"],
            releaseType=row["releaseType"],
            releasedBy=row["releasedBy"]) 
            for _, row in df.iterrows()]
    
    def get_release_mapping(self, path: str) -> dict[int, tuple[str, int]]:
        df = self.resource.load(file_path=path)
        return {row["releaseId"]: (row["releaseTitle"], row["releaseId"]) for _, row in df.iterrows()}