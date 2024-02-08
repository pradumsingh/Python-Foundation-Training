from UTIL.DB_Connection import DBConnection

class Cases(DBConnection):
    def __init__(self, case_id=None, description=None, case_date=None, status=None):
        self.case_id = case_id
        self.description = description
        self.case_date = case_date
        self.status = status

    def create_table(self):
        create_query = '''
            CREATE TABLE IF NOT EXISTS Cases (
            case_id INT PRIMARY KEY,
            description VARCHAR(150),
            case_date DATE,
            status VARCHAR(30)
            )'''
        try:
            self.getConnection()
            with self.connection.cursor() as cursor:
                cursor.execute(create_query)
            print("Case table created successfully")
        except Exception as e:
            print("Error creating case table:", e)

    def insert_into(self, case_id, description, case_date, status):
        insert_query = '''
            INSERT INTO Cases (case_id, description, case_date, status)
            VALUES (%s, %s, %s, %s)'''
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(insert_query, (case_id, description, case_date, status))
            self.connection.commit()
            print("Inserted successfully")
        except Exception as e:
            print("Error inserting into Cases:", e)

# Instantiate Cases object
cases = Cases()

# Create Cases table
cases.create_table()

# Inserting instances into Cases table
cases.insert_into(1, "Theft Case", "2024-02-08", "Active")
cases.insert_into(2, "Assault Case", "2024-02-06", "Closed")
cases.insert_into(3, "Fraud Case", "2024-02-05", "Active")
