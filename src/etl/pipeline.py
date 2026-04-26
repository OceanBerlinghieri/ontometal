import os

import pandas as pd

from etl.interactor.normalization.band_normalization import BandNormalization
from etl.interactor.normalization.country_normalization import CountryNormalization
from etl.interactor.normalization.genre_normalization import GenreNormalization
from etl.interactor.normalization.label_normalization import LabelNormalization
from etl.interactor.normalization.release_normalization import ReleaseNormalization
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
        print("Running...")

        working_dir = os.getcwd()
        # Data read
        distinct_genres = self.genre_repository.get_band_genres(
            path=os.path.join(working_dir, "src/etl/data/raw", "metal_bands_roster.csv")
        ).drop_duplicates().dropna()

        band_countries = self.country_repository.get_band_countries(
            path=os.path.join(working_dir, "src/etl/data/raw", "metal_bands_roster.csv")
        )

        label_countries = self.country_repository.get_label_countries(
            path=os.path.join(working_dir, "src/etl/data/raw", "labels_roster.csv")
        )

        releases = self.release_repository.get_releases(
            path=os.path.join(
                working_dir, "src/etl/data/raw", "all_bands_discography.csv"
            )
        )

        bands = self.band_repository.get_bands(
            path=os.path.join(working_dir, "src/etl/data/raw", "metal_bands_roster.csv")
        ).drop_duplicates()

        # Genres
        genre_normalization = GenreNormalization()
        normalized_genres = genre_normalization.normalize(distinct_genres)

        # Countries
        distinct_countries = (
            pd.concat([band_countries, label_countries]).drop_duplicates().dropna()
        )

        normalized_countries = CountryNormalization().normalize(distinct_countries)

        # Releases
        normalized_releases = ReleaseNormalization().normalize(releases, bands)

        # Labels
        labels = self.label_repository.get_labels(
            path=os.path.join(working_dir, "src/etl/data/raw", "labels_roster.csv")
        )

        normalized_labels = LabelNormalization().normalize(
            labels, normalized_countries, genre_normalization.genre_map
        )

        # Bands
        normalized_bands = BandNormalization().normalize(
            bands,
            normalized_countries,
            normalized_labels,
            genre_normalization.genre_map,
            normalized_releases,
        )

        # Save normalized datasets
        self.genre_repository.write_genres(
            normalized_genres,
            path=os.path.join(working_dir, "src/etl/data/normalized", "genres.csv"),
        )
        self.country_repository.write_countries(
            normalized_countries,
            path=os.path.join(working_dir, "src/etl/data/normalized", "countries.csv"),
        )
        self.release_repository.write_releases(
            normalized_releases,
            path=os.path.join(working_dir, "src/etl/data/normalized", "releases.csv"),
        )
        self.label_repository.write_labels(
            normalized_labels,
            path=os.path.join(working_dir, "src/etl/data/normalized", "labels.csv"),
        )
        self.band_repository.write_bands(
            normalized_bands,
            path=os.path.join(working_dir, "src/etl/data/normalized", "bands.csv"),
        )
