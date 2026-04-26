import re
from pandas import DataFrame

from src.etl.entities.genre import Genre


class GenreNormalization:
    def __init__(self):
        self.genre_map = {}

    def normalize(self, genres: DataFrame) -> DataFrame:
        # Split genres by common delimiters and expand to separate rows
        # Removes non-specific genres: "Heavy/Heavy Metal" -> ["Heavy Metal"]
        # But keeps both "Doom Metal" and "Extreme Doom Metal" (different subgenres)
        # Handles "/" and "," delimiters
        # Creates a mapping of genre variants to normalized names for later resolution on other datasets (e.g. label specializations)
        # Example: "Doom/Black Metal" -> ["Doom Metal", "Black Metal"]

        all_genres = self._split_into_all_genres(genres)

        all_genres = list(set(g.lower() for g in all_genres))

        filtered_global = self._filter_non_specific_genres(all_genres)

        self._build_genre_map(all_genres, filtered_global)

        normalized_genres = self._create_normalized_genres(all_genres, filtered_global)

        normalized_genres = DataFrame([vars(g) for g in normalized_genres])
        return normalized_genres.drop_duplicates(subset=["name"]).reset_index(drop=True)

    def _split_into_all_genres(self, genres: DataFrame) -> list[str]:
        all_genres = []

        for _, row in genres.iterrows():
            genre_str = str(row["Genre"]).strip()
            # Clean up genre string by removing details in parentheses, quotes, etc.
            cleaned_genre_str = re.sub(r"\(.*?\)|\'|’", "", genre_str)
            cleaned_genre_str = re.sub(r"\s+", " ", cleaned_genre_str).strip()

            split_genres = [
                g.strip() for g in cleaned_genre_str
                .replace(",", "/")
                .replace(";", "/")
                .replace(".", "/")
                .split("/") if g.strip() and len(g.strip()) > 3
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

    def _build_genre_map(self, all_unique: list[str], filtered: list[str]):
        for genre in filtered:
            self.genre_map[genre] = genre

        for genre in all_unique:
            if genre not in filtered:
                metal_form = genre + " metal"
                if metal_form in filtered:
                    self.genre_map[genre] = metal_form
                # If the genre is a substring of multiple "metal" genres, we can try to find the shortes match
                else:
                    best_match = None
                    for other in filtered:
                        if genre in other and "metal" in other:
                            if best_match is None or len(other) < len(best_match):
                                best_match = other
                    if best_match:
                        self.genre_map[genre] = best_match


    def _create_normalized_genres(self, all_genres: list[str], filtered_global: list[str]) -> list[Genre]:
        normalized_genres = []
        genre_id = 1

        for genre in all_genres:
            genre_lower = genre.lower()
            if genre_lower in filtered_global:
                normalized_genres.append(Genre(id=genre_id, name=genre_lower))
                genre_id += 1

        return normalized_genres