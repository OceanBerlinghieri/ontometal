import pandas as pd
from pandas import DataFrame
from etl.entities.band import Band


class BandNormalization:
    def __init__(self):
        pass

    def normalize(
        self,
        bands: DataFrame,
        countries: DataFrame,
        labels: DataFrame,
        genres: DataFrame,
        releases: DataFrame,
    ) -> DataFrame:
        normalized_bands = self._merge_countries(bands, countries)
        normalized_bands = self._merge_labels(normalized_bands, labels)
        normalized_bands = self._merge_genres(normalized_bands, genres)
        normalized_bands = self._merge_releases(normalized_bands, releases)
        normalized_bands = self._create_band_entities(normalized_bands)
        result = DataFrame([vars(b) for b in normalized_bands])
        return result

    def _merge_countries(self, labels, normalized_countries):
        labels["_country_lower"] = labels["Country"].str.strip().str.lower()
        labels = labels.merge(
            normalized_countries[["name"]],
            left_on="_country_lower",
            right_on="name",
            how="left",
        )
        labels = labels.drop(columns=["Country", "_country_lower"])
        labels = labels.rename(columns={"name": "country"})
        return labels

    def _merge_labels(self, bands, normalized_labels):
        bands = bands.merge(
            normalized_labels[["labelId"]].drop_duplicates(),
            left_on="Label ID",
            right_on="labelId",
            how="left",
        )
        bands = bands.drop(columns=["Label ID"])
        return bands.rename(columns={"labelId": "producedBy"})

    def _merge_genres(self, bands, genre_map: dict) -> DataFrame:
        def resolve_genres(genre_str):
            if pd.isna(genre_str) or not str(genre_str).strip():
                return [None]
            parts = [
                g.strip()
                for g in str(genre_str).replace(",", "/").split("/")
                if g.strip()
            ]
            resolved = [genre_map.get(p.strip().lower()) for p in parts]
            return [r for r in resolved if r] or [None]

        bands["genre"] = bands["Genre"].apply(resolve_genres)
        bands = bands.drop(columns=["Genre"])
        return bands

    def _merge_releases(self, bands: DataFrame, releases: DataFrame) -> DataFrame:
        releases_grouped = (
            releases.groupby("releasedBy")["releaseId"]
            .apply(list)
            .reset_index()
            .rename(columns={"releaseId": "releases"})
        )

        bands = bands.merge(
            releases_grouped, left_on="Band ID", right_on="releasedBy", how="left"
        )

        bands["releases"] = bands["releases"].apply(
            lambda x: x if isinstance(x, list) else []
        )
        bands = bands.drop(columns=["releasedBy"])
        return bands

    def _create_band_entities(self, bands: DataFrame) -> list[Band]:
        normalized_bands = []
        for _, row in bands.iterrows():
            normalized_bands.append(
                Band(
                    bandId=int(row["Band ID"]),
                    bandName=str(row["Name"]).strip().lower(),
                    status=str(row["Status"]).strip().lower(),
                    metalArchiveUrl=str(row["URL"]).strip().lower(),
                    releases=row["releases"],
                    producedBy=(
                        int(row["producedBy"]) if pd.notna(row["producedBy"]) else None
                    ),
                    hasGenre=row["genre"],
                    hasCountry=row["country"],
                )
            )

        return normalized_bands
