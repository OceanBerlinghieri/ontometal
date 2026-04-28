import os

from rdf_conversion import ONTOMETAL
from rdf_conversion.interactor.genre_converter import GenreConverter
from rdf_conversion.repository.resource.turtle_resource import TurtleResource
from rdflib import Graph

from rdf_conversion.interactor.country_converter import CountryConverter
from rdf_conversion.repository.country_repository import CountryRepository
from rdf_conversion.repository.genres_repository import GenreRepository


class Pipeline:
    def __init__(
        self, country_repository: CountryRepository, genre_repository: GenreRepository, turtle_resource: TurtleResource
    ):
        self.country_repository = country_repository
        self.genre_repository = genre_repository
        self.turtle_resource = turtle_resource

    def run(self):
        working_dir = os.getcwd()

        # Load base ontology skeleton
        ontology_path = os.path.join(
            working_dir, "ontology", "ontometal_skeleton.ttl"
        )
        graph = self.turtle_resource.load(ontology_path)
        graph.bind("om", ONTOMETAL)

        # Countries
        countries = self.country_repository.get_countries(
            path=os.path.join(
                working_dir, "src/etl/data/normalized", "countries_v2.csv"
            )
        )
        graph = CountryConverter().convert(countries, graph)

        # Genres
        genres = self.genre_repository.get_genres(
            path=os.path.join(
                working_dir, "src/etl/data/normalized", "genres_v2.csv"
            )
        )
        graph = GenreConverter().convert(genres, graph)

        # Save
        output_path = os.path.join(
            working_dir, "src/rdf_conversion/output", "ontometal.ttl"
        )
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.turtle_resource.save(graph, output_path)
        print(f"Saved to {output_path}")
