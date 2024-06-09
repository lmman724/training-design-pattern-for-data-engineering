from factories.database_factory import DatabaseFactory
from interfaces.database_interfaces import DatabaseConnectionInterface, DatabaseQueryInterface

from implementations.mysql_connection import MySQLConnection
from implementations.mysql_query import MySQLQuery

class MySQLFactory(DatabaseFactory):

    def create_instance(self):
        return self
    def create_connection(self) -> DatabaseConnectionInterface:
        return MySQLConnection()
    
    def create_query(self) -> DatabaseQueryInterface:
        return MySQLQuery()
    