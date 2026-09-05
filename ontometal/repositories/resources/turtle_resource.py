from rdflib import Graph

from ontometal.repositories.resources.base_resource import BaseResource


class TurtleResource(BaseResource):
    def __init__(self, config):
        super().__init__(config)

    def save(self, data: Graph) -> None:
        data.serialize(
            destination=self.config.get("APP", "OUTPUT_FILE"), format="turtle"
        )
