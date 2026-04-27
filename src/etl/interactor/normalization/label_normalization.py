import pandas as pd
from pandas import DataFrame

from etl.entities.label import Label
from etl.interactor.normalization.genre_utils import clean_and_split_genres


class LabelNormalization:
    def normalize(self, labels, normalized_countries, genre_map: dict) -> DataFrame:
        labels = self._merge_countries(labels, normalized_countries)
        labels = self._merge_specializations(labels, genre_map)
        labels = self._group_by_label(labels)

        labels = self._create_normalized_labels(labels)

        labels = DataFrame([vars(g) for g in labels])

        # Some labels may have float(NaN) in hasCountry. Convert to Int64 with NA support.
        labels["hasCountry"] = pd.to_numeric(labels["hasCountry"], errors='coerce').astype("Int64")
        return labels

    def _merge_countries(self, labels, normalized_countries):
        labels["_country_lower"] = labels["Country"].str.strip().str.lower()
        labels = labels.merge(
            normalized_countries[["name", "id"]],
            left_on="_country_lower",
            right_on="name",
            how="left",
        )
        labels = labels.drop(columns=["Country", "_country_lower", "name"])
        labels = labels.rename(columns={"id": "hasCountry"})

        return labels

    def _merge_specializations(self, labels, genre_map: dict):
        def resolve_uncomplete_genres(spec):
            if pd.isna(spec) or not str(spec).strip():
                return []
            parts = clean_and_split_genres(spec)
            resolved = [genre_map.get(p.strip().lower()) for p in parts]
            return [r for r in resolved if r] or []

        labels["specialization"] = labels["Specialization"].apply(
            resolve_uncomplete_genres
        )
        labels = labels.drop(columns=["Specialization"])

        return labels

    def _group_by_label(self, labels):
        # Raw CSV has one row per label-band pair (a label appears N times for N bands).
        # For duplicate Label IDs, prefer active status and most complete data.
        labels["_is_active"] = (labels["Status"].str.strip().str.lower() == "active").astype(int)
        labels["_completeness"] = labels.notna().sum(axis=1)
        labels = labels.sort_values(
            ["_is_active", "_completeness"], ascending=[False, False]
        )

        grouped = labels.groupby("Label ID", as_index=False).first()

        producer = (
            labels.dropna(subset=["Band ID"])
            .assign(**{"Band ID": labels["Band ID"].astype(int)})
            .groupby("Label ID")["Band ID"]
            .apply(lambda s: list(dict.fromkeys(int(x) for x in s)))
            .values
        )

        grouped["producer"] = producer

        return grouped.drop(columns=["Band ID", "_is_active", "_completeness"])

    def _create_normalized_labels(self, labels) -> list[Label]:
        normalized_labels = []

        for _, row in labels.iterrows():
            normalized_labels.append(
                Label(
                    labelId=int(row["Label ID"]),
                    labelName=str(row["Name"]).strip().lower(),
                    status=str(row["Status"]).strip().lower(),
                    websiteUrl=str(row["Website"]).strip().lower(),
                    producer=row["producer"],
                    hasCountry=(
                        int(row["hasCountry"]) if pd.notna(row["hasCountry"]) else None
                    ),
                    hasSpecialization=row["specialization"],
                )
            )
        return normalized_labels
