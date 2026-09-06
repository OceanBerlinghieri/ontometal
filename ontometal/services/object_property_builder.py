from rdflib import OWL, RDF, RDFS, Graph, Literal

from ontometal.entities.object_property_enum import (
    OBJECT_PROPERTY_METADATA,
    ObjectPropertyEnum,
)
from ontometal.services.graph_builder import GraphBuilder


class ObjectPropertyBuilder(GraphBuilder):
    def build(self, graph: Graph) -> Graph:
        for object_property in ObjectPropertyEnum:
            metadata = OBJECT_PROPERTY_METADATA[object_property]
            graph.add((object_property.value, RDF.type, OWL.ObjectProperty))

            if "sub_property_of" in metadata:
                graph.add(
                    (
                        object_property.value,
                        RDFS.subPropertyOf,
                        metadata["sub_property_of"],
                    )
                )

            if "type" in metadata:
                graph.add((object_property.value, RDF.type, metadata["type"]))

            for domain in metadata.get("domain", []):
                graph.add((object_property.value, RDFS.domain, domain))

            if "range" in metadata:
                graph.add((object_property.value, RDFS.range, metadata["range"]))

            if "comment" in metadata:
                graph.add(
                    (
                        object_property.value,
                        RDFS.comment,
                        Literal(metadata["comment"], lang="en"),
                    )
                )

            if "label" in metadata:
                graph.add(
                    (
                        object_property.value,
                        RDFS.label,
                        Literal(metadata["label"], lang="en"),
                    )
                )

        return graph
