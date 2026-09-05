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

            sub_property_of = metadata.get("sub_property_of")
            if sub_property_of is not None:
                graph.add((object_property.value, RDFS.subPropertyOf, sub_property_of))

            property_type = metadata.get("type")
            if property_type is not None:
                graph.add((object_property.value, RDF.type, property_type))

            for domain in metadata.get("domain", []):
                graph.add((object_property.value, RDFS.domain, domain))

            if "range" in metadata:
                graph.add((object_property.value, RDFS.range, metadata["range"]))

            if "comment" in metadata:
                graph.add(
                    (object_property.value, RDFS.comment, Literal(metadata["comment"]))
                )

            if "label" in metadata:
                graph.add(
                    (object_property.value, RDFS.label, Literal(metadata["label"]))
                )

        return graph
