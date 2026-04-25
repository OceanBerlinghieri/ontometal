import pandas as pd
from pandas import DataFrame

from etl.entities.label import Label


class LabelNormalization:
    def normalize(self, labels, normalized_countries, genre_map: dict) -> DataFrame:
        labels = self._merge_countries(labels, normalized_countries)
        labels = self._merge_specializations(labels, genre_map)

        normalized_labels = self._create_normalized_labels(labels)
        result = DataFrame([vars(g) for g in normalized_labels])
        return result.drop_duplicates(subset=["labelName"]).reset_index(drop=True)


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
    
    def _merge_specializations(self, labels, genre_map: dict):
        def resolve_uncomplete_genres(spec):
            if pd.isna(spec) or not str(spec).strip():
                return [None]
            parts = [
                g.strip() for g in str(spec).replace(",", "/").split("/") if g.strip()
            ]
            resolved = [genre_map.get(p.strip().lower()) for p in parts]
            return [r for r in resolved if r] or [None]

        labels["specialization"] = labels["Specialization"].apply(resolve_uncomplete_genres)
        labels = labels.explode("specialization").reset_index(drop=True)
        labels = labels.drop(columns=["Specialization"])

        return labels

    def _create_normalized_labels(self, labels) -> list[Label]:
        normalized_labels = []

        for _, row in labels.iterrows():
            normalized_labels.append(
                Label(
                    labelId=row["Label ID"],
                    labelName=str(row["Name"]).strip().lower(),
                    status=str(row["Status"]).strip().lower(),
                    websiteUrl=str(row["Website"]).strip().lower(),
                    producer=row["Band ID"],
                    hasCountry=row["country"],
                    hasSpecialization=row["specialization"],
                )
            )

        return normalized_labels
