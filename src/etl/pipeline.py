import os

import pandas as pd

from etl.repository.band_repository import BandRepository
from etl.repository.country_repository import CountryRepository
from etl.repository.genre_repository import GenreRepository
from etl.repository.label_repository import LabelRepository
from etl.repository.release_repository import ReleaseRepository


class Pipeline:
    def __init__(
        self,
        genre_repository: GenreRepository,
        country_repository: CountryRepository,
        release_repository: ReleaseRepository,
        label_repository: LabelRepository,
        band_repository: BandRepository,
    ):
        self.genre_repository = genre_repository
        self.country_repository = country_repository
        self.release_repository = release_repository
        self.label_repository = label_repository
        self.band_repository = band_repository

    def run(self):
        working_dir = os.getcwd()
        band_genres = self.genre_repository.get_band_genres(
            path=os.path.join(working_dir, "src/etl/raw", "metal_bands.csv")
        )

        label_specializations = self.genre_repository.get_label_specializations(
            path=os.path.join(working_dir, "src/etl/raw", "labels_roster.csv")
        )

        all_genres = (
            pd.concat([band_genres, label_specializations]).drop_duplicates().dropna()
        )

        print("All genres:")
        print(all_genres)
