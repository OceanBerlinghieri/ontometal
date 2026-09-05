from rdflib import DC, DCTERMS, OWL, RDF, RDFS, VANN, Graph, Literal, URIRef

from ontometal import OM
from ontometal.entities.ontology_metadata import OntologyMetadata
from ontometal.services.graph_builder import GraphBuilder


class OntologyMetadataBuilder(GraphBuilder):
    def __init__(self, ontology_metadata: OntologyMetadata):
        self.ontology_metadata = ontology_metadata

    def build(self, graph: Graph) -> Graph:
        ontology_uri = URIRef(OM)
        imports_uris = [
            URIRef(import_uri.strip())
            for import_uri in self.ontology_metadata.imports
            if import_uri.strip()
        ]

        graph.add((ontology_uri, RDF.type, OWL.Ontology))
        graph.add(
            (
                ontology_uri,
                OWL.versionIRI,
                URIRef(f"{ontology_uri}-{self.ontology_metadata.version}"),
            )
        )
        graph.add(
            (
                ontology_uri,
                OWL.versionInfo,
                Literal(self.ontology_metadata.version_info),
            )
        )
        graph.add((ontology_uri, DC.creator, Literal(self.ontology_metadata.creator)))
        graph.add((ontology_uri, DC.date, Literal(self.ontology_metadata.created)))
        graph.add(
            (
                ontology_uri,
                DC.contributor,
                Literal(self.ontology_metadata.contributor),
            )
        )
        graph.add(
            (
                ontology_uri,
                DC.publisher,
                Literal(self.ontology_metadata.publisher),
            )
        )
        graph.add((ontology_uri, DC.title, Literal(self.ontology_metadata.title)))
        graph.add(
            (
                ontology_uri,
                DCTERMS.license,
                Literal(self.ontology_metadata.license),
            )
        )
        graph.add(
            (
                ontology_uri,
                RDFS.comment,
                Literal(self.ontology_metadata.comment),
            )
        )
        graph.add(
            (
                ontology_uri,
                VANN.preferredNamespacePrefix,
                Literal(self.ontology_metadata.preferred_namespace_prefix),
            )
        )
        graph.add(
            (
                ontology_uri,
                VANN.preferredNamespaceUri,
                Literal(self.ontology_metadata.preferred_namespace_uri),
            )
        )

        for import_uri in imports_uris:
            graph.add((ontology_uri, OWL.imports, import_uri))

        return graph
