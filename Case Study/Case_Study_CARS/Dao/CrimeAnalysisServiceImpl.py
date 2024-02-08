from DBUtil.DB_Connection import DBConnection

class CrimeAnalysisServiceImpl:
    connection = None

    def __init__(self):
        if CrimeAnalysisServiceImpl.connection is None:
            CrimeAnalysisServiceImpl.connection = DBConnection.getConnection()



    @staticmethod
    def createIncident(incident):
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            cursor.execute(
                "INSERT INTO Incident (incident_type, incident_date, location, description, status, victim_id, suspect_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (incident.get_incident_type(), incident.get_incident_date(), incident.get_location(),
                 incident.get_description(), incident.get_status(), incident.get_victim_id(),
                 incident.get_suspect_id()))
            CrimeAnalysisServiceImpl.connection.commit()
            return True
        except Exception as e:
            print(f"Error creating incident: {e}")
            return False

    @staticmethod
    def updateIncidentStatus(status, incident_id):
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            cursor.execute("UPDATE Incident SET status = %s WHERE incident_id = %s", (status, incident_id))
            CrimeAnalysisServiceImpl.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating incident status: {e}")
            return False
    @staticmethod
    def getIncidentsInDateRange(start_date, end_date):
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            cursor.execute("SELECT * FROM Incident WHERE incident_date BETWEEN %s AND %s", (start_date, end_date))
            incidents = cursor.fetchall()
            return incidents
        except Exception as e:
            print(f"Error getting incidents in date range: {e}")
            return []

    @staticmethod
    def searchIncidents(criteria):
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            cursor.execute("SELECT * FROM Incident WHERE incident_type = %s", (criteria.get_type_name(),))
            incidents = cursor.fetchall()
            return incidents
        except Exception as e:
            print(f"Error searching incidents: {e}")
            return []

    @staticmethod
    def generateIncidentReport(incident):
        try:
            # Your implementation to generate incident report
            report_details = f"Report for incident {incident.incident_id}"
            return report_details
        except Exception as e:
            print(f"Error generating incident report: {e}")
            return None

    @staticmethod
    def createCase(case_description, incidents):
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            # Your implementation to create a new case and associate it with incidents
            cursor.execute("INSERT INTO `Cases` (case_description) VALUES (%s)", (case_description,))
            case_id = cursor.lastrowid
            for incident_id in incidents:
                cursor.execute("UPDATE `Cases` SET case_id = %s WHERE incident_id = %s", (case_id, incident_id))
            CrimeAnalysisServiceImpl.connection.commit()
            return case_id
        except Exception as e:
            print(f"Error creating case: {e}")
            return None

    @staticmethod
    def getCaseDetails(case_id):
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            cursor.execute("SELECT * FROM `Cases` WHERE case_id = %s", (case_id,))
            case_details = cursor.fetchone()
            return case_details
        except Exception as e:
            print(f"Error getting case details: {e}")
            return None

    @staticmethod
    def updateCaseDetails(case_id, case_description):
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            cursor.execute("UPDATE `Cases` SET case_description = %s WHERE case_id = %s", (case_description, case_id))
            CrimeAnalysisServiceImpl.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating case details: {e}")
            return False

    @staticmethod
    def getAllCases():
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            cursor.execute("SELECT * FROM `Cases`")
            cases = cursor.fetchall()
            return cases
        except Exception as e:
            print(f"Error getting all cases: {e}")
            return []
