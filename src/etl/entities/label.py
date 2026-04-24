from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from etl.entities.genre import Genre
from etl.entities.country import Country

if TYPE_CHECKING:
    from etl.entities.band import Band


@dataclass
class Label:
    # Data properties
    labelId: int
    labelName: str
    status: str
    websiteUrl: str
    # Object properties
    producer: Band  # noqa: F821
    hasSpecialization: Genre
    hasCountry: Country
