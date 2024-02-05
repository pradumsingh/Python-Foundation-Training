# db_connection.py

''' This class helps your program connect to a database. In simpler terms, imagine it as a tool that lets your program talk to the database and ask for information.
In this tool, there's a special room (variable) where
the program can go and connect to the database.'''

import mysql.connector
from mysql.connector import Error
from util.db_property_util import PropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            try:
                # Use the information from PropertyUtil to connect to the database
                connection_string = PropertyUtil.get_property_string()
                DBConnection.connection = mysql.connector.connect(**connection_string)

                if DBConnection.connection.is_connected():
                    print("Connected to MySQL database")
                else:
                    print("Failed to connect to MySQL database")

            except Error as e:
                print(f"Error: {e}")

        return DBConnection.connection
