from factories.mysql_factory import MySQLFactory
from factories.postgresql_factory import PostgreSQLFactory

def client_code(factory):

    create_user_id = "123"
    create_username = "example_user"
    connection = factory.create_connection()
    query = factory.create_query()

    # create_user = factory.create_user()
    update_user = factory.update_user(create_user_id)
    # delete_user = factory.delete_user()

    connection.connect()
    query.execute()


    # create_user.create_user(create_user_id, create_username)
    update_user.update_user(create_user_id)
    # delete_user.delete_user()
    connection.disconnect()

if __name__ == "__main__":
    print("Client: Testing client code with MySQLFactory:")
    client_code(MySQLFactory())

    # print("\nClient: Testing the same client code with PostgreSQLFactory:")
    # client_code(PostgreSQLFactory())

    print("\n ")
    client_code(MySQLFactory())