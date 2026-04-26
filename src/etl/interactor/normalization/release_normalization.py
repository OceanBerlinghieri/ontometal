from pandas import DataFrame

from etl.entities.band import Band
from etl.entities.release import Release


class ReleaseNormalization:
    def __init__(self):
        pass

    def normalize(self, releases: DataFrame, bands: DataFrame) -> DataFrame:
        normalized_releases = releases.merge(
            bands, left_on="Band ID", right_on="Band ID", how="left"
        )

        normalized_releases = self._create_release_entities(normalized_releases)
        normalized_releases = DataFrame([vars(r) for r in normalized_releases])
        return normalized_releases

    def _create_release_entities(self, releases_with_bands: DataFrame) -> list[Release]:
        normalized_releases = []
        for idx, (_, row) in enumerate(releases_with_bands.iterrows(), start=1):
            normalized_releases.append(
                Release(
                    releaseId=idx,
                    releaseTitle=str(row["Album Name"]).strip().lower(),
                    releaseYear=row["Year"],
                    releaseType=str(row["Type"]).strip().lower(),
                    releasedBy=int(row["Band ID"]),
                )
            )

        return normalized_releases
