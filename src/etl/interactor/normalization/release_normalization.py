from pandas import DataFrame

from etl.entities.band import Band
from etl.entities.release import Release


class ReleaseNormalization:
    def __init__(self):
        pass

    def normalize(self, releases: DataFrame, bands: DataFrame) -> DataFrame:
        releases_with_bands = releases.merge(
            bands, left_on="Band ID", right_on="Band ID", how="left"
        )

        normalized_releases = self._create_release_entities(releases_with_bands)
        result = DataFrame([vars(r) for r in normalized_releases])
        return result

    def _create_release_entities(self, releases_with_bands: DataFrame) -> list[Release]:
        normalized_releases = []
        for _, row in releases_with_bands.iterrows():
            normalized_releases.append(
                Release(
                    releaseTitle=str(row["Album Name"]).strip().lower(),
                    releaseYear=row["Year"],
                    releaseType=str(row["Type"]).strip().lower(),
                    releasedBy=row["Band ID"],
                )
            )

        return normalized_releases
