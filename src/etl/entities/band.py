from dataclasses import dataclass


@dataclass
class Band:
    # Data properties
    bandId: int
    bandName: str
    status: str
    metalArchiveUrl: str
    # Object properties
    releases: str  # List[Release]
    producedBy: int  # Label
    hasGenre: int  # Genre
    hasCountry: str  # Country
