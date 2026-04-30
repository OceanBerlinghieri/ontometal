import logging
import os

from rdf_conversion import ONTOMETAL
from rdf_conversion.interactor.genre_converter import GenreConverter
from rdf_conversion.interactor.label_converter import LabelConverter
from rdf_conversion.interactor.metadata_adder import MetadataAdder
from rdf_conversion.interactor.release_converter import ReleaseConverter
from rdf_conversion.repository.band_repository import BandRepository
from rdf_conversion.repository.label_repository import LabelRepository
from rdf_conversion.repository.release_repository_impl import ReleaseRepository
from rdf_conversion.repository.resource.turtle_resource import TurtleResource

from rdf_conversion.interactor.country_converter import CountryConverter
from rdf_conversion.repository.country_repository import CountryRepository
from rdf_conversion.repository.genres_repository import GenreRepository


logger = logging.getLogger(__name__)


class Pipeline:
    def __init__(
        self,
        country_repository: CountryRepository,
        genre_repository: GenreRepository,
        release_repository: ReleaseRepository,
        band_repository: BandRepository,
        label_repository: LabelRepository,
        turtle_resource: TurtleResource,
    ):
        self.country_repository = country_repository
        self.genre_repository = genre_repository
        self.release_repository = release_repository
        self.band_repository = band_repository
        self.label_repository = label_repository
        self.turtle_resource = turtle_resource

    def run(self):
        working_dir = os.getcwd()

        # Load base ontology skeleton
        logger.info("Loading skeleton")
        ontology_path = os.path.join(working_dir, "ontology", "ontometal_skeleton.ttl")
        graph = self.turtle_resource.load(ontology_path)
        graph.bind("om", ONTOMETAL)

        # Ontology metadata
        graph = MetadataAdder().add_metadata(graph)

        # Countries
        logger.info("Converting countries")
        countries = self.country_repository.get_countries(
            path=os.path.join(
                working_dir, "src/etl/data/normalized", "countries_v2.csv"
            )
        )
        graph = CountryConverter().convert(countries, graph)

        # Genres
        logger.info("Converting genres")
        genres = self.genre_repository.get_genres(
            path=os.path.join(working_dir, "src/etl/data/normalized", "genres_v2.csv")
        )
        graph = GenreConverter().convert(genres, graph)

        # Releases
        logger.info("Converting releases")
        releases = self.release_repository.get_releases(
            path=os.path.join(
                working_dir, "src/etl/data/normalized", "releases_v2.csv"
            )
        )

        band_mapping = self.band_repository.get_band_mapping(
            path=os.path.join(
                working_dir, "src/etl/data/normalized", "bands_v2.csv"
            )
        )
        graph = ReleaseConverter().convert(releases, band_mapping, graph)

        # Labels
        logger.info("Converting labels")
        labels = self.label_repository.get_labels(
            path=os.path.join(
                working_dir, "src/etl/data/normalized", "labels_v2.csv"
            )
        )

        genre_mapping = self.genre_repository.get_genre_mapping(
            path=os.path.join(
                working_dir, "src/etl/data/normalized", "genres_v2.csv"
            )
        )

        country_mapping = self.country_repository.get_country_mapping(
            path=os.path.join(
                working_dir, "src/etl/data/normalized", "countries_v2.csv"
            )
        )

        graph = LabelConverter().convert(labels, band_mapping, genre_mapping, country_mapping, graph)


        # Save
        logger.info("Saving output")
        output_path = os.path.join(
            working_dir, "src/rdf_conversion/output", "ontometal.ttl"
        )
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.turtle_resource.save(graph, output_path)
