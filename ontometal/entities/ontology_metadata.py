from dataclasses import dataclass, field


@dataclass(frozen=True)
class OntologyMetadata:
    uri: str
    version: str
    version_info: str
    creator: str
    created: str
    contributor: str
    publisher: str
    title: str
    license: str
    comment: str
    preferred_namespace_prefix: str
    preferred_namespace_uri: str
    imports: list[str] = field(default_factory=list)
