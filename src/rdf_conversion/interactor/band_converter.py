from rdflib import Graph, Literal, RDF, XSD
import pandas as pd

from etl.entities.band import Band
from rdf_conversion import ONTOMETAL, sanitize_uri_fragment


class BandConverter:
    def convert(self, 
                bands: list[Band],
                label_mapping: dict[int, tuple[str, int]],
                genre_mapping: dict[int, tuple[str, int]],
                release_mapping: dict[int, tuple[str, int]],
                country_mapping: dict[int, tuple[str, int]],
                graph: Graph) -> Graph:
        for band in bands:
            band_uri = ONTOMETAL[f"{sanitize_uri_fragment(band.bandName)}_{band.bandId}"]

            graph.add((band_uri, RDF.type, ONTOMETAL.Band))
            graph.add((band_uri, ONTOMETAL.bandName, Literal(band.bandName.title(), datatype=XSD.string)))
            graph.add((band_uri, ONTOMETAL.status, Literal(band.status.title(), datatype=XSD.string)))
            graph.add((band_uri, ONTOMETAL.metalArchiveUrl, Literal(band.metalArchiveUrl, datatype=XSD.string)))

            for release in band.releases:
                if release not in release_mapping:
                    continue
                release_name, release_id = release_mapping[release]
                release_uri = ONTOMETAL[f"{sanitize_uri_fragment(release_name)}_{release_id}" ]
                graph.add((band_uri, ONTOMETAL.releases, release_uri))
            
            if band.producedBy not in label_mapping:
                continue
            label_name, label_id = label_mapping[band.producedBy]
            label_uri = ONTOMETAL[f"{sanitize_uri_fragment(label_name)}_{label_id}" ]
            graph.add((band_uri, ONTOMETAL.producedBy, label_uri))
        
            for genre in band.hasGenre:
                if genre not in genre_mapping:
                    continue
                genre_name, genre_id = genre_mapping[genre]
                genre_uri = ONTOMETAL[f"{sanitize_uri_fragment(genre_name)}_{genre_id}" ]
                graph.add((band_uri, ONTOMETAL.hasGenre, genre_uri))


            if not pd.isna(band.hasCountry):
                country_name, country_id = country_mapping[band.hasCountry]
                country_uri = ONTOMETAL[f"{sanitize_uri_fragment(country_name)}_{country_id}"]
                graph.add((band_uri, ONTOMETAL.hasCountry, country_uri))

        return graph