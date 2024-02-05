# dao/crime_analysis_service_impl.py
from util.db_conn import DBConnection
from entity.incident import Incident
from entity.report import Report
from entity.case import Case
from dao.icrime_analysis_service import ICrimeAnalysisService
import datetime  # Import datetime module for handling dates
from exception import incident_number_not_found_exception
from exception.incident_number_not_found_exception import IncidentNumberNotFoundException
class CrimeAnalysisServiceImpl(ICrimeAnalysisService):
    connection = DBConnection.get_connection()

    def create_incident(self, incident):
        try:
            with self.connection.cursor() as cursor:
                # Modify your SQL query to exclude the 'IncidentID' column
                sql = "INSERT INTO Incidents (IncidentType, IncidentDate, Location, Description, Status, VictimID, SuspectID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (
                    incident.incident_type,
                    incident.incident_date,
                    incident.location,
                    incident.description,
                    incident.status,
                    incident.victim_id,
                    incident.suspect_id
                ))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error creating incident: {e}")
            return False

    @staticmethod
    def update_incident_status(status, incident_id):
        try:
            # Implement the logic to update the status of an incident in the database
            with CrimeAnalysisServiceImpl.connection.cursor() as cursor:
                sql = "UPDATE Incidents SET Status = %s WHERE IncidentID = %s"
                cursor.execute(sql, (status, incident_id))
            CrimeAnalysisServiceImpl.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating incident status: {e}")
            return False

    @staticmethod
    def get_incidents_in_date_range(start_date, end_date):
        try:
            # Implement the logic to get a list of incidents within a date range from the database
            with CrimeAnalysisServiceImpl.connection.cursor() as cursor:
                sql = "SELECT * FROM Incidents WHERE IncidentDate BETWEEN %s AND %s"
                cursor.execute(sql, (start_date, end_date))
                incidents = cursor.fetchall()
                return [Incident(*incident) for incident in incidents]
        except Exception as e:
            print(f"Error getting incidents in date range: {e}")
            return []

    @staticmethod
    def get_incident_details(incident_number):
        try:
            # Implement the logic to get incident details from the database
            with CrimeAnalysisServiceImpl.connection.cursor() as cursor:
                sql = "SELECT * FROM Incidents WHERE IncidentID = %s"
                cursor.execute(sql, (incident_number,))
                incident_details = cursor.fetchone()

                if incident_details:
                    return Incident(*incident_details)
                else:
                    # If incident not found, raise a generic exception
                    raise Exception(f"Incident with number {incident_number} not found.")
        except Exception as e:
            # Handle the exception
            print(f"Exception: {e}")
            return None
    @staticmethod
    def update_case_details(case):
        try:
            # Implement the logic to update case details in the database
            with CrimeAnalysisServiceImpl.connection.cursor() as cursor:
                sql = "UPDATE Cases SET CaseDescription = %s WHERE CaseID = %s"
                cursor.execute(sql, (case.case_description, case.case_id))
            CrimeAnalysisServiceImpl.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating case details: {e}")
            return False

    @staticmethod
    def get_all_cases():
        try:
            # Implement the logic to get a list of all cases from the database
            with CrimeAnalysisServiceImpl.connection.cursor() as cursor:
                sql = "SELECT * FROM Cases"
                cursor.execute(sql)
                cases = cursor.fetchall()
                return [Case(*case) for case in cases]
        except Exception as e:
            print(f"Error getting all cases: {e}")
            return []

    @staticmethod
    def search_incidents(criteria):
        try:
            # Implement the logic to search incidents based on criteria in the database
            # Replace the following line with your implementation
            return []
        except Exception as e:
            print(f"Error searching incidents: {e}")
            return []

    @staticmethod
    def generate_incident_report(incident):
        try:
            # Implement the logic to generate an incident report in the database
            # Replace the following line with your implementation
            return None
        except Exception as e:
            print(f"Error generating incident report: {e}")
            return None

    @staticmethod
    def create_case(case_description, incidents):
        try:
            # Implement the logic to create a new case and associate it with incidents in the database
            # Replace the following line with your implementation
            return None
        except Exception as e:
            print(f"Error creating case: {e}")
            return None

    @staticmethod
    def get_case_details(case_id):
        try:
            # Implement the logic to get details of a specific case from the database
            # Replace the following line with your implementation
            return None
        except Exception as e:
            print(f"Error getting case details: {e}")
            return None