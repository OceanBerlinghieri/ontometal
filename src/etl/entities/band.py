from dataclasses import dataclass


@dataclass
class Band:
    # Data properties
    bandId: int
    bandName: str
    status: str
    metalArchiveUrl: str
    # Object properties
    releases: list  # TODO: Change to list[int] once Release has releaseId
    producedBy: int  # Label.labelId
    hasGenre: list[str]  # Genre names (resolved via genre_map)
    hasCountry: str  # TODO: Change to int once Country has id
