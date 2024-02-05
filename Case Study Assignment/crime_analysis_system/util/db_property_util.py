# property_util.py


'''This class helps your program get the details it needs
to connect to the database. In simpler terms, think of
it as a helper that reads a note (property file)
containing important details like the name of the
 house (database), the key to the house (username), etc.
 It then  hands over this information to the DBConnection tool.'''
# main_module.py
import mysql.connector
from mysql.connector import Error
import configparser

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

class PropertyUtil:
    @staticmethod
    def get_property_string():
        # Set the provided details directly in the method
        connection_string = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Batman@123#',
            'database': 'crime_analysis_system',
            'port': '3306'
        }

        return connection_string

def main():
    # Establish a connection to the database
    connection = DBConnection.get_connection()

    # Your application logic goes here
    # ...

if __name__ == "__main__":
    main()
