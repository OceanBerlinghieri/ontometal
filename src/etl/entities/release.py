from dataclasses import dataclass

from etl.entities.band import Band

@dataclass
class Release:
    #Data properties
    releaseTitle: str
    releaseYear: int
    #Object properties
    releasedBy: Band