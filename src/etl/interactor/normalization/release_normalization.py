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
                    releaseTitle=row["Album Name"],
                    releaseYear=row["Year"],
                    releaseType=row["Type"],
                    releasedBy=Band(
                        bandId=row["Band ID"],
                        bandName=row["Name"],
                        status=row["Status"],
                        metalArchiveUrl=row["URL"],
                        releases=None,  # This will be set in the Band normalization step
                        producedBy=None,  # This will be set in the Band normalization step
                        hasGenre=None,  # This will be set in the Band normalization step
                        hasCountry=None,  # This will be set in the Band normalization step
                    ),
                )
            )

        return normalized_releases
