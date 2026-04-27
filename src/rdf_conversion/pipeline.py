import os

from rdf_conversion import ONTOMETAL
from rdf_conversion.repository.resource.turtle_resource import TurtleResource
from rdflib import Graph

from rdf_conversion.interactor.country_converter import CountryConverter
from rdf_conversion.repository.country_repository import CountryRepository


class Pipeline:
    def __init__(
        self, country_repository: CountryRepository, turtle_resource: TurtleResource
    ):
        self.country_repository = country_repository
        self.turtle_resource = turtle_resource

    def run(self):
        working_dir = os.getcwd()

        # Load existing ontology from output
        ontology_path = os.path.join(
            working_dir, "src/rdf_conversion/output", "ontometal.ttl"
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

        print(f"Graph has {len(graph)} triples")

        # Save
        output_path = os.path.join(
            working_dir, "src/rdf_conversion/output", "ontometal.ttl"
        )
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.turtle_resource.save(graph, output_path)
        print(f"Saved to {output_path}")
