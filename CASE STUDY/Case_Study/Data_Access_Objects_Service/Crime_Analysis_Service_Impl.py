from UTIL.DB_Connection import DBConnection

class CrimeAnalysisService:
    def __init__(self):
        self.db_connection = DBConnection()

    def create_incident(self):
        start_date = input("Enter the start date(yyyy-mm-dd): ")
        end_date = input("Enter the input date(yyyy-mm-dd): ")
        incidents = self.db_connection.get_incidents_in_date_range(start_date, end_date)
        for incident in incidents:
            print(incident)

    def search_incidents(self):
        incident_id = int(input('Enter the incident id to search the incident details: '))
        incidents = self.db_connection.search_incidents(incident_id)
        for incident in incidents:
            print(incident)
        print("Search successful")

    def generate_incident_report(self):
        incident_id = int(input("Enter the incident id to generate a report: "))
        reports = self.db_connection.generate_incident_report(incident_id)
        for report in reports:
            print(report)
        print("Reports generated successfully")

    def create_case(self):
        case_id = int(input("Enter the case id: "))
        description = input("Enter the description: ")
        case_date = input("Enter the case date: ")
        status = input("Enter the status: ")
        self.db_connection.create_case(case_id, description, case_date, status)
        print("Created case successfully")

    def get_case_details(self):
        case_id = int(input("Enter the case Id to get details: "))
        case_details = self.db_connection.get_case_details(case_id)
        for detail in case_details:
            print(detail)
        print("Case details displayed successfully")

    def update_case_details(self):
        case_id = int(input("Enter the case Id to update details: "))
        description = input("Enter the description: ")
        case_date = input("Enter the case date: ")
        status = input("Enter the status: ")
        self.db_connection.update_case_details(case_id, description, case_date, status)
        print("Case updated successfully")

    def get_all_cases(self):
        cases = self.db_connection.get_all_cases()
        for case in cases:
            print(case)
