from rdflib import Graph, Literal, URIRef, OWL, XSD

from rdf_conversion import ONTOMETAL_VERSION, ONTOMETAL_VERSION_INFO


class MetadataAdder:
    def add_metadata(self, graph: Graph) -> Graph:
        ontology_uri = URIRef("https://w3id.org/ontometal")
        graph.add(
            (
                ontology_uri,
                OWL.versionIRI,
                Literal(ONTOMETAL_VERSION, datatype=XSD.string),
            )
        )
        graph.add(
            (
                ontology_uri,
                OWL.versionInfo,
                Literal(ONTOMETAL_VERSION_INFO, datatype=XSD.string),
            )
        )

        return graph
