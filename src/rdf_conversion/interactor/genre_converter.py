from pandas import DataFrame
from rdflib import Graph, Literal, RDF, XSD

from rdf_conversion import ONTOMETAL


class GenreConverter:
    def convert(self, genres: DataFrame, graph: Graph) -> Graph:
        for _, row in genres.iterrows():
            genre_uri = ONTOMETAL[f"{row['name'].title().replace(' ', '')}"]
            graph.add((genre_uri, RDF.type, ONTOMETAL.Genre))
            graph.add((genre_uri, ONTOMETAL.genreName, Literal(row["name"], datatype=XSD.string)))

        return graph