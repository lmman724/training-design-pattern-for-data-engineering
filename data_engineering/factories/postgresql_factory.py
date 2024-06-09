from factories.database_factory import DatabaseFactory
from interfaces.database_interfaces import DatabaseConnectionInterface, DatabaseQueryInterface
from implementations.postgresql_connection import PostgreSQLConnection
from implementations.postgresql_query import PostgreSQLQuery

class PostgreSQLFactory(DatabaseFactory):

    def create_instance(self):
        return self
    def create_connection(self) -> DatabaseConnectionInterface:
        return PostgreSQLConnection()
    
    def create_query(self) -> DatabaseQueryInterface:
        return PostgreSQLQuery()
