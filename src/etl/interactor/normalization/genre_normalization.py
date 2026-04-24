from pandas import DataFrame
import pandas as pd
from src.etl.entities.genre import Genre


class GenreNormalization:
    def __init__(self):
        pass

    def normalize(self, genres: DataFrame) -> DataFrame:
        # Split genres by common delimiters and expand to separate rows
        # Removes non-specific genres: "Heavy/Heavy Metal" -> ["Heavy Metal"]
        # But keeps both "Doom Metal" and "Extreme Doom Metal" (different subgenres)
        # Handles "/" and "," delimiters
        # Example: "Doom/Black Metal" -> ["Doom Metal", "Black Metal"]

        all_genres = self._split_into_all_genres(genres)

        unique_genres = list(set(g.lower() for g in all_genres))

        filtered_global = self._filter_non_specific_genres(unique_genres)

        normalized_genres = self._create_normalized_genres(all_genres, filtered_global)

        result = pd.DataFrame([vars(g) for g in normalized_genres])
        return result.drop_duplicates(subset=["name"]).reset_index(drop=True)

    def _split_into_all_genres(self, genres: DataFrame) -> list[str]:
        all_genres = []

        for idx, row in genres.iterrows():
            genre_str = str(row["Genre"]).strip()
            split_genres = [
                g.strip() for g in genre_str.replace(",", "/").split("/") if g.strip()
            ]
            all_genres.extend(split_genres)
        return all_genres

    def _filter_non_specific_genres(self, genres: list[str]) -> list[str]:
        unique_genres = list(set(g.lower() for g in genres))
        filtered_global = []

        for genre in unique_genres:
            has_metal = "metal" in genre

            should_remove = False
            if not has_metal:
                for other in unique_genres:
                    if other != genre and "metal" in other and genre in other:
                        should_remove = True
                        break

            if not should_remove:
                filtered_global.append(genre)

        return filtered_global

    def _create_normalized_genres(self, all_genres: list[str], filtered_global: list[str]) -> list[Genre]:
        normalized_genres = []
        genre_id = 1

        for genre in all_genres:
            genre_lower = genre.lower()
            if genre_lower in filtered_global:
                normalized_genres.append(Genre(id=genre_id, name=genre))
                genre_id += 1

        return normalized_genres