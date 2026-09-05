from enum import Enum

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
    OM.bandId: {"label": "Band ID", "comment": "The unique identifier for a band"},
    OM.bandName: {"label": "Band Name", "comment": "The name of the band"},
    OM.bandStatus: {
        "label": "Band Status",
        "comment": "The current status of the band",
    },
    OM.countryName: {"label": "Country Name", "comment": "The name of the country"},
    OM.genreId: {"label": "Genre ID", "comment": "The unique identifier for a genre"},
    OM.genreName: {"label": "Genre Name", "comment": "The name of the genre"},
    OM.labelId: {"label": "Label ID", "comment": "The unique identifier for a label"},
    OM.labelName: {"label": "Label Name", "comment": "The name of the label"},
    OM.labelStatus: {
        "label": "Label Status",
        "comment": "The current status of the label",
    },
    OM.labelWebsiteUrl: {
        "label": "Label Website URL",
        "comment": "The URL of the label's website",
    },
    OM.metalArchivesUrl: {
        "label": "Metal Archives URL",
        "comment": "The URL of the band's page on Metal Archives",
    },
    OM.releaseTitle: {"label": "Release Title", "comment": "The title of the release"},
    OM.releaseYear: {
        "label": "Release Year",
        "comment": "The year the release was published",
    },
    OM.url: {"label": "URL", "comment": "The URL associated with the entity"},
}
