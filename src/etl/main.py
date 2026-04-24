from etl.pipeline import Pipeline
from etl.repository import country_repository
from etl.repository.band_repository_impl import BandRepositoryImpl
from etl.repository.country_repository_impl import CountryRepositoryImpl
from etl.repository.genre_repository_impl import GenreRepositoryImpl
from etl.repository.label_repository_impl import LabelRepositoryImpl
from etl.repository.release_repository_impl import ReleaseRepositoryImpl
from etl.repository.resource.csv_resource import CSVResource

if __name__ == "__main__":
    # Resource
    resource = CSVResource()
    # Repositories
    genre_repository = GenreRepositoryImpl(resource=resource)
    country_repository = CountryRepositoryImpl(resource=resource)
    label_repository = LabelRepositoryImpl(resource=resource)
    release_repository = ReleaseRepositoryImpl(resource=resource)
    band_repository = BandRepositoryImpl(resource=resource)
    pipeline = Pipeline(
        genre_repository=genre_repository,
        country_repository=country_repository,
        release_repository=release_repository,
        label_repository=label_repository,
        band_repository=band_repository,
    )
    pipeline.run()
