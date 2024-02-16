from Util.Db_Connection import DBConnection


class Reports(DBConnection):
    def __init__(self, report_id=None, incident_id=None, report_date=None, report_details=None, status=None, officer_id=None):
        self.report_id = report_id
        self.incident_id = incident_id
        self.report_date = report_date
        self.report_details = report_details
        self.status = status
        self.officer_id= officer_id

    def create_table(self):
        create_query = '''
        create table if not exists Reports(
        report_id int primary key,
        incident_id int,
        report_date date,
        report_details varchar(150),
        status varchar(200),
        officer_id int,
        FOREIGN KEY (incident_id) REFERENCES Incidents(incident_id),
        FOREIGN KEY (officer_id) REFERENCES Officers(officer_id)
        )'''
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(create_query)
        print("Reports table successfully created")

    def insert_into(self):
        self.report_id = int(input("Enter the report id: "))
        self.incident_id = int(input("Enter the incident id: "))
        self.report_date = input("Enter the report date: ")
        self.report_details = input("Enter the report details: ")
        self.status = input("Enter the status: ")
        self.officer_id = int(input("Enter the officer_id: "))

        insert_query = 'INSERT INTO Reports(report_id, incident_id, report_date, report_details, status, officer_id) VALUES (%s, %s, %s, %s, %s, %s)'
        data = (self.report_id, self.incident_id, self.report_date, self.report_details, self.status, self.officer_id)

        connection = DBConnection.getConnection()
        cursor = connection.cursor()

        cursor.execute(insert_query, data)

        connection.commit()
        print("Values inserted successfully")

    def update_table(self):
        try:
            self.report_id = int(input("Enter the report id: "))
            self.incident_id = input("Enter the incident id: ")
            self.officer_id = int(input("Enter the officer_id: "))
            self.report_date = input("Enter the report date: ")
            self.report_details = input("Enter the report details: ")
            self.status = input("Enter the status: ")

            update_query = 'update Reports set incident_id=%s, officer_id=%s, report_date=%s, report_details=%s, status=%s where report_id=%s'
            data = (self.incident_id, self.officer_id, self.report_date, self.report_details, self.status,self.report_id)
            DBConnection.getConnection()
            stmt = DBConnection.connection.cursor()
            stmt.execute(update_query, data)
            DBConnection.connection.commit()
            print("Values updated successfully")

        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_table(self):
        self.report_id = int(input("Enter the report id to delete values: "))
        delete_query = f'delete from Reports where report_id={self.report_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(delete_query)
        DBConnection.connection.commit()
        print("Values deleted successfully")

    def select_table(self):
        select_query = 'select * from Reports'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(select_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Values displayed successfully")