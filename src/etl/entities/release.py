from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from etl.entities.band import Band


@dataclass
class Release:
    # TODO: Add releaseId: int (auto-incremented). Store release IDs in Band.releases instead of title strings.
    # Data properties
    releaseTitle: str
    releaseYear: int
    releaseType: str
    # Object properties
    releasedBy: int  # noqa: F821
