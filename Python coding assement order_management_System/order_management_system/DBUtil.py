import mysql.connector

class DBUtil:
    """Establishes and manages a connection to the MySQL database."""

    def __init__(self):
        self.hostname = "localhost"
        self.port = 3306
        self.username = "root"
        self.password = "Batman@123#"  # Replace with your actual password
        self.database_name = "order_management_system"  # Replace with your database name
        self.connection = None

    def get_db_conn(self):
        """Establishes a connection to the MySQL database and returns the connection object."""
        try:
            if self.connection is None:
                self.connection = mysql.connector.connect(
                    host=self.hostname,
                    port=self.port,
                    user=self.username,
                    password=self.password,
                    database=self.database_name
                )
                print("Database connection established.")
            return self.connection

        except mysql.connector.Error as e:
            print("Database connection failed:", e)
            return None

    def close_connection(self):
        """Closes the database connection, if open."""
        if self.connection is not None:
            self.connection.close()
            print("Database connection closed.")
            self.connection = None

if __name__ == "__main__":
    # Test the connection (optional)
    db_util = DBUtil()
    conn = db_util.get_db_conn()
    if conn:
        # Test queries or database operations here
        # ...
        db_util.close_connection()
