from enum import Enum

from rdflib import FOAF, OWL

from ontometal import OM
from ontometal.repositories.namespaces_import import AO


class ObjectPropertyEnum(Enum):
    has_country = OM.hasCountry
    has_genre = OM.hasGenre
    has_specialization = OM.hasSpecialization
    produced_by = OM.producedBy
    producer = OM.producer
    released_by = OM.releasedBy
    releases = OM.releases


OBJECT_PROPERTY_METADATA = {
    ObjectPropertyEnum.has_country: {
        "sub_property_of": FOAF.based_near,
        "type": OWL.FunctionalProperty,
        "domain": [OM.Band, OM.Label],
        "range": OM.Country,
        "comment": "Indicates the country associated with an entity",
        "label": "Has Country",
    },
    ObjectPropertyEnum.has_genre: {
        "sub_property_of": AO.genre,
        "type": OWL.TransitiveProperty,
        "domain": [OM.Band],
        "range": OM.Genre,
        "comment": "Indicates the genre associated with an entity",
        "label": "Has Genre",
    },
    ObjectPropertyEnum.has_specialization: {
        "sub_property_of": AO.genre,
        "type": OWL.TransitiveProperty,
        "domain": [OM.Label],
        "range": OM.Genre,
        "comment": "Indicates the specialization associated with an entity",
        "label": "Has Specialization",
    },
    ObjectPropertyEnum.produced_by: {
        "type": OWL.TransitiveProperty,
        "domain": [OM.Band],
        "range": OM.Label,
        "comment": "Indicates an entity produced by another entity",
        "label": "Produced By",
    },
    ObjectPropertyEnum.producer: {
        "domain": [OM.Label],
        "range": OM.Band,
        "comment": "Indicates the producer of an entity",
        "label": "Producer",
    },
    ObjectPropertyEnum.released_by: {
        "sub_property_of": FOAF.made,
        "inverse_of": OM.releases,
        "type": OWL.FunctionalProperty,
        "domain": [OM.Release],
        "range": OM.Band,
        "comment": "Indicates the entity that released another entity",
        "label": "Released By",
    },
    ObjectPropertyEnum.releases: {
        "sub_property_of": FOAF.maker,
        "inverse_of": OM.releasedBy,
        "domain": [OM.Band],
        "range": OM.Release,
        "comment": "Indicates the entity that is released by another entity",
        "label": "Releases",
    },
}
