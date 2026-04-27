from pandas import DataFrame
from rdflib import Graph, Literal, RDF, XSD

from rdf_conversion import ONTOMETAL


class CountryConverter:
    def convert(self, countries: DataFrame, graph: Graph) -> Graph:
        for _, row in countries.iterrows():
            country_uri = ONTOMETAL[f"{row['name'].title().replace(' ', '')}"]
            graph.add((country_uri, RDF.type, ONTOMETAL.Country))
            graph.add((country_uri, ONTOMETAL.countryName, Literal(row["name"], datatype=XSD.string)))

        return graph