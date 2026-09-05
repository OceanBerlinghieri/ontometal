from rdflib import OWL, RDF, RDFS, Graph, Literal

from ontometal.entities.data_property_enum import (
    DATA_PROPERTY_METADATA,
    DataPropertyEnum,
)
from ontometal.services.graph_builder import GraphBuilder


class DataPropertyBuilder(GraphBuilder):
    def build(self, graph: Graph) -> Graph:
        for data_property in DataPropertyEnum:
            metadata = DATA_PROPERTY_METADATA[data_property.value]

            graph.add((data_property.value, RDF.type, OWL.DatatypeProperty))
            graph.add((data_property.value, RDFS.comment, Literal(metadata["comment"])))
            graph.add((data_property.value, RDFS.label, Literal(metadata["label"])))
        return graph
