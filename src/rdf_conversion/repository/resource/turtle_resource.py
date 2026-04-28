from rdflib import Graph

from rdf_conversion.repository.resource.base_resource import BaseResource


class TurtleResource(BaseResource):
    def load(self, file_path: str, **kwargs) -> Graph:
        graph = Graph()
        graph.parse(file_path, format="turtle")
        return graph

    def save(self, data: Graph, file_path: str) -> None:
        data.serialize(destination=file_path, format="turtle")
