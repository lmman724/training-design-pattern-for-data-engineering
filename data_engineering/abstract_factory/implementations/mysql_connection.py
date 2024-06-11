from interfaces.database_interfaces import DatabaseConnectionInterface

import mysql.connector
class MySQLConnection(DatabaseConnectionInterface):
    def connect(self):

        self.connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "example",
            database = "test_db"
        )

        print("Connecting to MySQL database")

    def disconnect(self) -> None:
        print("Disconnecting from MySQL database")

