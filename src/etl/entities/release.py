from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from etl.entities.band import Band


@dataclass
class Release:
    # Data properties
    releaseTitle: str
    releaseYear: int
    releaseType: str
    # Object properties
    releasedBy: Band  # noqa: F821
