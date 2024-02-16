from Util.Db_Connection import DBConnection
from Data_Access_Objects.I_crime_analysis_service import I_crime_analysis_service
from Entity.Incidents import Incidents
from Entity.Reports import Reports
from Entity.Case import Cases


class crime_analysis_service_impl(Incidents, Reports, Cases, DBConnection, I_crime_analysis_service):
    def __init__(self):
        super(Incidents, self).__init__()

    def createIncident(self):
        incident = Incidents()
        incident.insert_into()

    def updateIncidentStatus(self):
        incident = Incidents()
        incident.update_table()

    def getIncidentsInDateRange(self):
        try:
            start_date = input("Enter the start date(yyyy-mm-dd): ")
            end_date = input("Enter the end date(yyyy-mm-dd): ")

            # Assuming DBConnection.getConnection() establishes a connection to your database
            DBConnection.getConnection()
            cursor = DBConnection.connection.cursor()

            select_query = "SELECT * FROM Incidents WHERE incident_date BETWEEN %s AND %s"
            cursor.execute(select_query, (start_date, end_date))
            incidents = cursor.fetchall()

            for incident in incidents:
                print(incident)

        except Exception as e:
            print(f"An error occurred: {e}")

    def searchIncidents(self):
        self.incident_id = int(input('Enter the incident id to search the incident details: '))
        search_query = f'select * from Incidents where incident_id = {self.incident_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(search_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Searched successfully")

    def generateIncidentReport(self):
        self.incident_id = int(input("Enter the incident id to generate a report: "))
        report_query = f'select * from Reports where incident_id = {self.incident_id}'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(report_query)
        data = stmt.fetchall()
        for i in data:
            print(i)
        print("Reports generated successfully")

    def createCase(self):
        # self.case_id = int(input("Enter the case id: "))
        # self.description = input("Enter the description: ")
        # self.case_date = input("Enter the case date: ")
        # self.status = input("Enter the status: ")
        print("Table already exists")



    def create_table(self):
        query = 'insert into Cases(case_id, description, case_date, status) values(%s,%s,%s,%s)'
        data = [(self.case_id, self.description, self.case_date, self.status)]
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.executemany(query, data)
        DBConnection.connection.commit()
        print("Created case successfully")

    def getCaseDetails(self):
        try:
            self.case_id = int(input("Enter the case Id to get details: "))
            get_query = f'select * from Cases where case_id={self.case_id}'
            DBConnection.getConnection()
            stmt = DBConnection.connection.cursor()
            stmt.execute(get_query)
            data = stmt.fetchall()
            if not data:
                print("No case found with the given ID.")
            else:
                for i in data:
                    print(i)
                print("Case details displayed successfully")
            DBConnection.connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def updateCaseDetails(self):
        try:
            self.case_id = int(input("Enter the case Id to update details: "))
            self.description = input("Enter the description: ")
            self.case_date = input("Enter the case date: ")
            self.status = input("Enter the status: ")
            update_query = 'update Cases set description=%s, case_date=%s, status=%s where case_id=%s'
            values = (self.description, self.case_date, self.status, self.case_id)
            DBConnection.getConnection()
            stmt = DBConnection.connection.cursor()
            stmt.execute(update_query, values)
            DBConnection.connection.commit()
            print("Case updated successfully")
        except Exception as e:
            print(f"An error occurred: {e}")

    def getAllCases(self):
        get_query = f'select * from Cases'
        DBConnection.getConnection()
        stmt = DBConnection.connection.cursor()
        stmt.execute(get_query)
        data = stmt.fetchall()
        for i in data:
            print(i)



# obj = crime_analysis_service_impl()
# obj.generateIncidentReport()
