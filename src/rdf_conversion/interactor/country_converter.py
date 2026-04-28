from rdflib import Graph, Literal, RDF, XSD

from etl.entities.country import Country
from rdf_conversion import ONTOMETAL


class CountryConverter:
    def convert(self, countries: list[Country], graph: Graph) -> Graph:
        for country in countries:
            country_uri = ONTOMETAL[f"{country.name.title().replace(' ', '')}"]
            graph.add((country_uri, RDF.type, ONTOMETAL.Country))
            graph.add((country_uri, ONTOMETAL.countryName, Literal(country.name, datatype=XSD.string)))

        return graph