from rdflib import Graph, Literal, RDF, XSD
import pandas as pd

from etl.entities.label import Label
from rdf_conversion import ONTOMETAL, sanitize_uri_fragment

class LabelConverter:
    def convert(self, 
                labels: list[Label], 
                band_mapping: dict[int, tuple[str, int]],
                genre_mapping: dict[int, tuple[str, int]],
                country_mapping: dict[int, tuple[str, int]],
                graph: Graph) -> Graph:
        for label in labels:
            label_uri = ONTOMETAL[f"{sanitize_uri_fragment(label.labelName)}_{label.labelId}"]

            graph.add((label_uri, RDF.type, ONTOMETAL.Label))
            graph.add((label_uri, ONTOMETAL.labelName, Literal(label.labelName.title(), datatype=XSD.string)))
            graph.add((label_uri, ONTOMETAL.status, Literal(label.status.title(), datatype=XSD.string)))
            graph.add((label_uri, ONTOMETAL.websiteUrl, Literal(label.websiteUrl, datatype=XSD.string)))

            for producer_id in label.producer:
                if producer_id not in band_mapping:
                    continue
                band_name, band_id = band_mapping[producer_id]
                producer_uri = ONTOMETAL[f"{sanitize_uri_fragment(band_name)}_{band_id}" ]
                graph.add((label_uri, ONTOMETAL.producer, producer_uri))
            
            for specialization in label.hasSpecialization:
                if specialization not in genre_mapping:
                    continue
                genre_name, genre_id = genre_mapping[specialization]
                genre_uri = ONTOMETAL[f"{sanitize_uri_fragment(genre_name)}_{genre_id}" ]
                graph.add((label_uri, ONTOMETAL.hasSpecialization, genre_uri))

            if not pd.isna(label.hasCountry):
                country_name, country_id = country_mapping[label.hasCountry]
                country_uri = ONTOMETAL[f"{sanitize_uri_fragment(country_name)}_{country_id}"]
                graph.add((label_uri, ONTOMETAL.hasCountry, country_uri))
        return graph