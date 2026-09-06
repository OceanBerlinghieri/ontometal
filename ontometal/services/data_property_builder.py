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

            if "sub_property_of" in metadata:
                graph.add(
                    (
                        data_property.value,
                        RDFS.subPropertyOf,
                        metadata["sub_property_of"],
                    )
                )

            if "type" in metadata:
                graph.add((data_property.value, RDF.type, metadata["type"]))

            for domain in metadata.get("domain", []):
                graph.add((data_property.value, RDFS.domain, domain))

            if "range" in metadata:
                graph.add((data_property.value, RDFS.range, metadata["range"]))

            graph.add(
                (
                    data_property.value,
                    RDFS.comment,
                    Literal(metadata["comment"], lang="en"),
                )
            )
            graph.add(
                (data_property.value, RDFS.label, Literal(metadata["label"], lang="en"))
            )
        return graph
