from enum import Enum

from rdflib import DCTERMS, FOAF, OWL, XSD

from ontometal import OM


class DataPropertyEnum(Enum):
    band_id = OM.bandId
    band_name = OM.bandName
    band_status = OM.bandStatus
    country_name = OM.countryName
    genre_id = OM.genreId
    genre_name = OM.genreName
    label_id = OM.labelId
    label_name = OM.labelName
    label_status = OM.labelStatus
    label_website_url = OM.labelWebsiteUrl
    metal_archives_url = OM.metalArchivesUrl
    release_title = OM.releaseTitle
    release_year = OM.releaseYear
    url = OM.url


DATA_PROPERTY_METADATA = {
    OM.bandId: {
        "sub_property_of": DCTERMS.identifier,
        "type": OWL.FunctionalProperty,
        "domain": [OM.Band],
        "range": XSD.long,
        "label": "Band ID",
        "comment": "The unique identifier for a band",
    },
    OM.bandName: {
        "sub_property_of": FOAF.name,
        "domain": [OM.Band],
        "range": XSD.string,
        "label": "Band Name",
        "comment": "The name of the band",
    },
    OM.bandStatus: {
        "sub_property_of": FOAF.status,
        "type": OWL.FunctionalProperty,
        "domain": [OM.Band],
        "range": XSD.string,
        "label": "Band Status",
        "comment": "The current status of the band",
    },
    OM.countryName: {
        "sub_property_of": FOAF.name,
        "domain": [OM.Country],
        "range": XSD.string,
        "label": "Country Name",
        "comment": "The name of the country",
    },
    OM.genreId: {
        "sub_property_of": DCTERMS.identifier,
        "domain": [OM.Genre],
        "range": XSD.long,
        "label": "Genre ID",
        "comment": "The unique identifier for a genre",
    },
    OM.genreName: {
        "sub_property_of": FOAF.name,
        "domain": [OM.Genre],
        "range": XSD.string,
        "label": "Genre Name",
        "comment": "The name of the genre",
    },
    OM.labelId: {
        "sub_property_of": DCTERMS.identifier,
        "type": OWL.FunctionalProperty,
        "domain": [OM.Label],
        "range": XSD.long,
        "label": "Label ID",
        "comment": "The unique identifier for a label",
    },
    OM.labelName: {
        "sub_property_of": FOAF.name,
        "domain": [OM.Label],
        "range": XSD.string,
        "label": "Label Name",
        "comment": "The name of the label",
    },
    OM.labelStatus: {
        "sub_property_of": FOAF.status,
        "domain": [OM.Label],
        "range": XSD.string,
        "label": "Label Status",
        "comment": "The current status of the label",
    },
    OM.labelWebsiteUrl: {
        "sub_property_of": OM.url,
        "domain": [OM.Label],
        "range": XSD.string,
        "label": "Label Website URL",
        "comment": "The URL of the label's website",
    },
    OM.metalArchivesUrl: {
        "sub_property_of": OM.url,
        "domain": [OM.Band],
        "range": XSD.string,
        "label": "Metal Archives URL",
        "comment": "The URL of the band's page on Metal Archives",
    },
    OM.releaseTitle: {
        "sub_property_of": DCTERMS.title,
        "domain": [OM.Release],
        "range": XSD.string,
        "label": "Release Title",
        "comment": "The title of the release",
    },
    OM.releaseYear: {
        "equivalent_property": DCTERMS.available,
        "sub_property_of": DCTERMS.date,
        "domain": [OM.Release],
        "range": XSD.gYear,
        "label": "Release Year",
        "comment": "The year the release was published",
    },
    OM.url: {"label": "URL", "comment": "The URL associated with the entity"},
}
