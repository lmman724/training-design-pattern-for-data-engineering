from abc import ABC, abstractmethod

from interfaces.database_interfaces import DatabaseConnectionInterface, DatabaseQueryInterface
from interfaces.user_management_interfaces import UserManagementInterface

class DatabaseFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DatabaseConnectionInterface:
        pass

    @abstractmethod
    def create_query(self) -> DatabaseQueryInterface:
        pass

    @abstractmethod
    def create_user(self) -> UserManagementInterface:
        pass

    @abstractmethod
    def update_user(self, user_id) -> UserManagementInterface:
        pass

    @abstractmethod
    def delete_user(self, user_id) -> UserManagementInterface:
        pass