from factories.mysql_factory import MySQLFactory
from factories.postgresql_factory import PostgreSQLFactory

def client_code(factory):
    connection = factory.create_connection()
    query = factory.create_query()

    connection.connect()
    query.execute()

if __name__ == "__main__":
    # print("Client: Testing client code with MySQLFactory:")
    # client_code(MySQLFactory())

    print("\nClient: Testing the same client code with PostgreSQLFactory:")
    client_code(PostgreSQLFactory())