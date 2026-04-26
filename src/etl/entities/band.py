from dataclasses import dataclass


@dataclass
class Band:
    # Data properties
    bandId: int
    bandName: str
    status: str
    metalArchiveUrl: str
    # Object properties
    releases: list[int]  # List of Release.releaseId
    producedBy: int  # Label.labelId
    hasGenre: list[str]  # Genre names (resolved via genre_map)
    hasCountry: int  # Country.countryId