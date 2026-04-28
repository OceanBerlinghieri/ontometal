from rdflib import Graph, Literal, RDF, XSD

from etl.entities.genre import Genre
from rdf_conversion import ONTOMETAL


class GenreConverter:
    def convert(self, genres: list[Genre], graph: Graph) -> Graph:
        for genre in genres:
            genre_uri = ONTOMETAL[f"{genre.name.title().replace(' ', '')}"]
            graph.add((genre_uri, RDF.type, ONTOMETAL.Genre))
            graph.add((genre_uri, ONTOMETAL.genreName, Literal(genre.name, datatype=XSD.string)))

        return graph