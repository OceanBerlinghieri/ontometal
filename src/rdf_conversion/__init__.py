import re
import unicodedata

from rdflib import Namespace

ONTOMETAL = Namespace("https://w3id.org/ontometal#")
ONTOMETAL_VERSION = "1.0.0"
ONTOMETAL_VERSION_INFO = "First complete version of the ontology"


def sanitize_uri_fragment(name: str) -> str:
    # Keep only alphanumeric and underscores
    name = name.title().replace(' ', '')
    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
    name = re.sub(r'[^A-Za-z0-9_]', '', name)
    return name
