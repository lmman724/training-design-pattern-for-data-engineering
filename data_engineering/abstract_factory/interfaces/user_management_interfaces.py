from abc import ABC, abstractmethod

class UserManagementInterface(ABC):
    @abstractmethod
    def create_user(self) -> None:
        pass

    @abstractmethod
    def update_user(self) -> None:
        pass

    @abstractmethod
    def delete_user(self) -> None:
        pass