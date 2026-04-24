from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from etl.entities.country import Country
from etl.entities.genre import Genre
from etl.entities.release import Release

if TYPE_CHECKING:
    from etl.entities.label import Label


@dataclass
class Band:
    # Data properties
    bandId: int
    bandName: str
    status: str
    metalArchiveUrl: str
    # Object properties
    releases: Optional[Release]
    producedBy: Optional[Label]  # noqa: F821
    hasGenre: Optional[Genre]
    hasCountry: Optional[Country]
