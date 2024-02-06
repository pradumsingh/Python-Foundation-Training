import mysql
from mysql import connector


class DBUtil:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="Batman@123#",
            database="techshop"
        )

    def getDBConnection(self):
        return self.con.cursor()