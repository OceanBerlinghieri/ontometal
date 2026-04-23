from etl.pipeline import Pipeline
from etl.repository.band_repository_impl import BandRepositoryImpl
from etl.repository.resource.csv_resource import CSVResource

if __name__ == "__main__":
    # Repositories
    band_repository = BandRepositoryImpl(resource=CSVResource())
    pipeline = Pipeline(
        band_repository=band_repository
        )
    pipeline.run()