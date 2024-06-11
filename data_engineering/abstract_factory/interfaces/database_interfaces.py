from abc import ABC, abstractmethod

class DatabaseConnectionInterface(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

class DatabaseQueryInterface(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass