from abc import ABC, abstractmethod


class BaseSessionCreator(ABC):
    @abstractmethod
    def create_session(self, db_uri: str):
        raise NotImplementedError()
