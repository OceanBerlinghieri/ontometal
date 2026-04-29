from pandas import DataFrame
import pandas as pd
from etl.entities.release import Release


class ReleaseNormalization:
    def __init__(self):
        pass

    def normalize(self, releases: DataFrame, bands: DataFrame) -> DataFrame:
        releases = releases.dropna(subset=["Album Name"])
        releases = releases[
            ~releases["Album Name"].str.strip().str.lower().isin(["null"])
        ]

        # Drop releases with non-numeric years
        releases = releases[pd.to_numeric(releases["Year"], errors="coerce").notna()]

        # Keep only bands that will survive band normalization
        # (no null names, no duplicate Band IDs) to avoid orphan releases
        valid_bands = bands.dropna(subset=["Name"])
        valid_bands = valid_bands[
            ~valid_bands["Name"].str.strip().str.lower().isin(["null"])
        ]
        valid_bands = valid_bands.drop_duplicates(subset=["Band ID"], keep=False)

        normalized_releases = releases.merge(
            valid_bands, left_on="Band ID", right_on="Band ID", how="inner"
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
                    releaseYear=int(row["Year"]),
                    releaseType=str(row["Type"]).strip().lower(),
                    releasedBy=int(row["Band ID"]),
                )
            )

        return normalized_releases
