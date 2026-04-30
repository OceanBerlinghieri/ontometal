
import logging

from rdf_conversion.pipeline import Pipeline
from rdf_conversion.repository.country_repository_impl import CountryRepositoryImpl
from rdf_conversion.repository.label_repository_impl import LabelRepositoryImpl
from rdf_conversion.repository.release_repository_impl import ReleaseRepositoryImpl
from rdf_conversion.repository.band_repository_impl import BandRepositoryImpl
from rdf_conversion.repository.genres_repository_impl import GenreRepositoryImpl
from rdf_conversion.repository.resource.csv_resource import CSVResource
from rdf_conversion.repository.resource.turtle_resource import TurtleResource

if __name__ == "__main__":
    # Config
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Resources
    csv_resource = CSVResource()
    turtle_resource = TurtleResource()
    
    # Repositories
    country_repository = CountryRepositoryImpl(resource=csv_resource)
    genre_repository = GenreRepositoryImpl(resource=csv_resource)
    release_repository = ReleaseRepositoryImpl(resource=csv_resource)
    band_repository = BandRepositoryImpl(resource=csv_resource)

    pipeline = Pipeline(
        country_repository=country_repository,
        genre_repository=genre_repository,
        release_repository=release_repository,
        band_repository=band_repository,
        label_repository=LabelRepositoryImpl(resource=csv_resource),
        #TODO create ttl repository
        turtle_resource=turtle_resource,
    )
    pipeline.run()
