from dataclasses import dataclass


@dataclass
class Label:
    # Data properties
    labelId: int
    labelName: str
    status: str
    websiteUrl: str
    # Object properties
    producer: int  # Band.bandId
    hasSpecialization: str  # Genre name (resolved via genre_map)
    hasCountry: str  # TODO: Change to int once Country has id
