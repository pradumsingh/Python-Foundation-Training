import mysql.connector

class DBConnection:
    __connection = None

    @staticmethod
    def getConnection():
        if not DBConnection.__connection:
            connection_string = {
                'host': 'localhost',
                'user': 'root',
                'password': 'Batman@123#',
                'database': 'crime_analysis_reporting_system',
                'port': 3306
            }
            try:
                DBConnection.__connection = mysql.connector.connect(**connection_string)
                print("Connected to MySQL database")
            except mysql.connector.Error as e:
                print(f"Error connecting to MySQL database: {e}")
        return DBConnection.__connection