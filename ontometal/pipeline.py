from rdflib import Graph

from ontometal.repositories.resources.base_resource import BaseResource
from ontometal.services.graph_builder import GraphBuilder


class Pipeline:
    def run(
        self,
        turtle_resource: BaseResource,
        ontology_metadata_adder: GraphBuilder,
        class_builder: GraphBuilder,
        data_property_builder: GraphBuilder,
        object_property_builder: GraphBuilder,
    ) -> None:
        graph = Graph()
        ontology_metadata_adder.build(graph)

        # Classes
        class_builder.build(graph)

        # Data Properties
        data_property_builder.build(graph)

        # Object Properties
        object_property_builder.build(graph)

        # Save the graph to a Turtle file
        turtle_resource.save(graph)
