from interfaces.user_management_interfaces import UserManagementInterface

import mysql.connector
class MySQLUserManagement(UserManagementInterface):

    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "example",
            database = "test_db"
        )
        self.cursor = self.connection.cursor()

    def create_user(self, user_id, username):
        print("Creating user in MySQL database")
        self.cursor.execute("INSERT INTO users (user_id, username) VALUES (%s, %s)", (user_id, username))
        self.connection.commit()

    def update_user(self, user_id):
        print("Updating user in MySQL database")
        self.cursor.execute("UPDATE users SET username = 'new_username' WHERE user_id = %s", (user_id,))
        self.connection.commit()

    def delete_user(self, user_id):
        print("Deleting user in MySQL database")
        self.cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        self.connection.commit()