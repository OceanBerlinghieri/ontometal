from dataclasses import dataclass


@dataclass
class Label:
    # Data properties
    labelId: int
    labelName: str
    status: str
    websiteUrl: str
    # Object properties
    producer: int  # Band
    hasSpecialization: int  # Genre
    hasCountry: str  # Country
