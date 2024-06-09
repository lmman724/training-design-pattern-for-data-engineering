from abc import ABC, abstractmethod

from interfaces.database_interfaces import DatabaseConnectionInterface, DatabaseQueryInterface

class DatabaseFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DatabaseConnectionInterface:
        pass

    @abstractmethod
    def create_query(self) -> DatabaseQueryInterface:
        pass