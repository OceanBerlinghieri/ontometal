from rdflib import URIRef
from rdflib.namespace import DefinedNamespace, Namespace


class OM(DefinedNamespace):
    """
    Ontology Metadata (OM) namespace.
    This namespace is used to define metadata properties for ontologies.
    """

    _uri = "https://w3id.org/ontometal#"

    # https://w3id.org/ontometal#properties
    hasCountry: URIRef
    hasGenre: URIRef
    producedBy: URIRef
    producer: URIRef
    hasSpecialization: URIRef
    releasedBy: URIRef
    releases: URIRef
    releaseType: URIRef

    # https://w3id.org/ontometal#dataproperties
    bandId: URIRef
    bandName: URIRef
    bandStatus: URIRef
    countryName: URIRef
    genreId: URIRef
    genreName: URIRef
    labelId: URIRef
    labelName: URIRef
    labelStatus: URIRef
    labelWebsiteUrl: URIRef
    metalArchivesUrl: URIRef
    releaseTitle: URIRef
    releaseYear: URIRef
    url: URIRef

    # https://w3id.org/ontometal#classes
    Band: URIRef
    Country: URIRef
    Genre: URIRef
    Label: URIRef
    MetalGenre: URIRef
    Release: URIRef

    _NS = Namespace(_uri)
