from dataclasses import dataclass


@dataclass
class Country:
    # TODO: Add id: int (auto-incremented). Use it as FK in Band and Label instead of name string.
    # Data properties
    name: str
