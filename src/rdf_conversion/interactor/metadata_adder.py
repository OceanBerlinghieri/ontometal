from rdflib import Graph, Literal, URIRef, OWL, XSD

from rdf_conversion import ONTOMETAL_VERSION, ONTOMETAL_VERSION_INFO


class MetadataAdder:
    def add_metadata(self, graph: Graph) -> Graph:
        ontology_uri = URIRef("https://w3id.org/ontometal")

        graph.remove((ontology_uri, OWL.versionIRI, None))
        graph.remove((ontology_uri, OWL.versionInfo, None))

        graph.add(
            (
                ontology_uri,
                OWL.versionIRI,
                Literal(f"{ontology_uri}-{ONTOMETAL_VERSION}"),
            )
        )
        graph.add(
            (
                ontology_uri,
                OWL.versionInfo,
                Literal(f"{ONTOMETAL_VERSION_INFO}"),
            )
        )

        return graph
