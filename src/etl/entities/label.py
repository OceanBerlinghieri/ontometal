from dataclasses import dataclass

from etl.entities.band import Band
from etl.entities.genre import Genre
from etl.entities.country import Country


@dataclass
class Label:
    # Data properties
    labelId: int
    labelName: str
    status: str
    websiteUrl: str
    # Object properties
    producer: Band
    hasSpecialization: Genre
    hasCountry: Country
