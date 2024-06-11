from factories.database_factory import DatabaseFactory
from interfaces.database_interfaces import DatabaseConnectionInterface, DatabaseQueryInterface
from interfaces.user_management_interfaces import UserManagementInterface

from implementations.mysql_connection import MySQLConnection
from implementations.mysql_query import MySQLQuery
from implementations.mysql_user_management import MySQLUserManagement
class MySQLFactory(DatabaseFactory):

    def create_instance(self):
        return self
    def create_connection(self) -> DatabaseConnectionInterface:
        return MySQLConnection()
    
    def create_query(self) -> DatabaseQueryInterface:
        return MySQLQuery()
    
    def create_user(self) -> UserManagementInterface:
        return MySQLUserManagement()
    
    def update_user(self, user_id) -> UserManagementInterface:
        return MySQLUserManagement()
    
    def delete_user(self, user_id) -> UserManagementInterface:
        return MySQLUserManagement()
    

    
    