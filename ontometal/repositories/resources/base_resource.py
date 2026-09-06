from abc import ABC, abstractmethod


class BaseResource(ABC):

    def __init__(self, config):
        self.config = config

    @abstractmethod
    def save(self, data) -> None:
        pass
