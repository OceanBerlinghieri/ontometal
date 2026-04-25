from dataclasses import dataclass


@dataclass
class Label:
    # Data properties
    labelId: int
    labelName: str
    status: str
    websiteUrl: str
    # Object properties
    producer: list[int]  # List of Band.bandId
    hasSpecialization: list[str]  # Genre name (resolved via genre_map)
    hasCountry: int # Country.countryId
