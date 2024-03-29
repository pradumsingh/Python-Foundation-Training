from Util.Db_Connection import DBConnection


class Evidence(DBConnection):
    def __init__(self, evidence_id=None, description=None, location=None, incident_id=None):
        self.evidence_id = evidence_id
        self.description = description
        self.location = location
        self.incident_id = incident_id

    def create_table(self):
        create_query = '''
        CREATE TABLE IF NOT EXISTS Evidence(
        evidence_id INT PRIMARY KEY,
        description VARCHAR(150),
        location VARCHAR(50),
        incident_id INT,
        FOREIGN KEY (incident_id) REFERENCES Incidents(incident_id)
        )'''
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(create_query)
        print("Evidence table created successfully")

    def insert_into(self):
        self.evidence_id = int(input("Enter the evidence id: "))
        self.description = input("Enter the description: ")
        self.location = input("Enter the location: ")
        self.incident_id = input("Enter the incident id: ")

        insert_query = 'insert into Evidence(evidence_id, description, location, incident_id) values(%s,%s,%s,%s)'
        data = [(self.evidence_id, self.description, self.location, self.incident_id)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(insert_query, data)
        DBConnection.connection.commit()
        print("Values inserted successfully")

    def update_table(self):
        try:
            self.evidence_id = int(input("Enter the evidence id: "))
            self.description = input("Enter the description: ")
            self.location = input("Enter the location: ")
            self.incident_id = input("Enter the incident id: ")

            update_query = 'update Evidence set description=%s, location=%s, incident_id=%s where evidence_id=%s'
            data = (self.description, self.location, self.incident_id, self.evidence_id)  # Removed list wrapping data
            DBConnection.getConnection()
            stmt = DBConnection.connection.cursor()
            stmt.execute(update_query, data)
            DBConnection.connection.commit()
            print("Values updated successfully")

        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_table(self):
        self.evidence_id = int(input("Enter the evidence id to delete values: "))
        delete_query = f'delete from Evidence where evidence_id={self.evidence_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(delete_query)
        DBConnection.connection.commit()
        print("Values deleted successfully")

    def select_table(self):
        select_query = 'select * from Evidence'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(select_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Values displayed successfully")