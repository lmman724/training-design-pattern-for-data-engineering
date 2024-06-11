import unittest
from unittest.mock import MagicMock, patch

import sys
import os
# sys.path.append('data_engineering/abstract_factory/implementations')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import patch
from implementations.mysql_connection import MySQLConnection

class TestMySQLFactory(unittest.TestCase):
    
    @patch("mysql.connector.connect")
    def setUp(self, mock_connect):
        self.connection = MySQLConnection()
        self.mock_connection_instance = MagicMock()
        mock_connect.return_value = self.mock_connection_instance
        self.connection = MySQLConnection()
    
    @patch("mysql.connector.connect")
    def test_connect(self, mock_connect):
            self.connection.connect()
            mock_connect.assert_called_once_with(
                host="localhost",
                user = "root",
                password = "example",
                database = "test_db"
            )
            print("test_connect passed")

    # @patch("mysql.connector.connect")
    # def test_disconnect(self, mock_connect):
    #         # mock_connect = mock_connect.return_value
    #         self.connection.connect()
    #         self.connection.connection = self.mock_connection_instance
    #         self.connection.disconnect()
    #         self.mock_connection_instance.close.assert_called_once()
    #         print("test_disconnect passed")

if __name__ == "__main__":
    unittest.main()
