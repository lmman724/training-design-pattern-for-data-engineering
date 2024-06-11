from interfaces.database_interfaces import DatabaseConnectionInterface
import mysql.connector

class MySQLQuery(DatabaseConnectionInterface):

    def __init__(self):
        self.connection = None
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user = "root",
                password = "example",
                database = "test_db"
            )
            print("Connecting to MySQL database")
        except mysql.connector.Error as error:
            print(f"Failed to connect to MySQL database: {error}")

    def execute(self) -> None:
        print("Executing PostgreSQL query")

