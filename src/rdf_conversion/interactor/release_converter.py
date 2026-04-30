from rdflib import Graph, Literal, RDF, XSD

from etl.entities.band import Band
from etl.entities.release import Release
from rdf_conversion import ONTOMETAL, sanitize_uri_fragment


class ReleaseConverter:
    def convert(self, releases: list[Release], band_map: dict[int, tuple[str, int]], graph: Graph) -> Graph:
        for release in releases:
            band_name, band_id = band_map[release.releasedBy]
            band_uri = ONTOMETAL[f"{sanitize_uri_fragment(band_name)}_{band_id}"]

            release_uri = ONTOMETAL[f"{sanitize_uri_fragment(release.releaseTitle)}_{release.releaseId}"]
            graph.add((release_uri, RDF.type, ONTOMETAL.Release))
            graph.add((release_uri, ONTOMETAL.releaseTitle, Literal(release.releaseTitle.title(), datatype=XSD.string)))
            graph.add((release_uri, ONTOMETAL.releaseYear, Literal(release.releaseYear, datatype=XSD.gYear)))
            graph.add((release_uri, ONTOMETAL.releaseType, Literal(release.releaseType, datatype=XSD.string)))
            graph.add((release_uri, ONTOMETAL.releasedBy, band_uri))

        return graph