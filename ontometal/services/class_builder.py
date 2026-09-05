from rdflib import OWL, RDF, RDFS, Graph, Literal

from ontometal.entities.class_enum import CLASS_METADATA, ClassEnum
from ontometal.services.graph_builder import GraphBuilder


class ClassBuilder(GraphBuilder):
    def build(self, graph: Graph) -> Graph:
        for class_name in ClassEnum:
            metadata = CLASS_METADATA[class_name.value]
            graph.add((class_name.value, RDF.type, OWL.Class))
            graph.add((class_name.value, RDFS.label, Literal(metadata["label"])))
            graph.add((class_name.value, RDFS.comment, Literal(metadata["comment"])))
        return graph
