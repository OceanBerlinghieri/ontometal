from dataclasses import dataclass

from etl.entities.country import Country
from etl.entities.genre import Genre
from etl.entities.label import Label
from etl.entities.release import Release


@dataclass
class Band:
    # Data properties
    bandId: int
    bandName: str
    status: str
    metalArchiveUrl: str
    # Object properties
    releases: Release
    producedBy: Label
    hasGenre: Genre
    hasCountry: Country
