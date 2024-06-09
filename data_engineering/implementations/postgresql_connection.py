from interfaces.database_interfaces import DatabaseConnectionInterface

import psycopg2

class PostgreSQLConnection(DatabaseConnectionInterface):
    def connect(self):
        self.connection = psycopg2.connect(
            host="localhost",
            user = "postgres",
            password = "example",
            database= "test_db"
        )
        print("Connecting to MySQL database")

    def disconnect(self) -> None:
        print("Disconnecting from MySQL database")
