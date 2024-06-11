from interfaces.database_interfaces import DatabaseConnectionInterface
import psycopg2

class PostgreSQLQuery(DatabaseConnectionInterface):
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host="localhost",
                user="postgres",
                password="example",
                database="test_db"
            )
            print("Connected to PostgreSQL database")
        except psycopg2.Error as error:
            print(f"Failed to connect to PostgreSQL database: {error}")

    def execute(self) -> None:
        print("Executing PostgreSQL query")