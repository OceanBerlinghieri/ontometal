from abc import ABC, abstractmethod
from rdflib import Graph


class GraphBuilder(ABC):
    @abstractmethod
    def build(self, graph: Graph) -> Graph:
        pass
