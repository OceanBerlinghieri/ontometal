from enum import Enum

from ontometal import OM


class ClassEnum(Enum):
    band = OM.Band
    country = OM.Country
    genre = OM.Genre
    label = OM.Label
    metal_genre = OM.MetalGenre
    release = OM.Release


CLASS_METADATA = {
    OM.Band: {
        "label": "Band",
        "comment": "A musical group or artist entity.",
    },
    OM.Country: {
        "label": "Country",
        "comment": "A country associated with a band or release.",
    },
    OM.Genre: {
        "label": "Genre",
        "comment": "A musical genre associated with a band or release.",
    },
    OM.Label: {
        "label": "Label",
        "comment": "A record label associated with a band or release.",
    },
    OM.MetalGenre: {
        "label": "Metal Genre",
        "comment": "A specific subgenre of metal music.",
    },
    OM.Release: {
        "label": "Release",
        "comment": "A musical release, such as an album or single.",
    },
}
