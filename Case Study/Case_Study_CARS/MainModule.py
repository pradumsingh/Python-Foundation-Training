from Dao.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from Entity.Incident import Incident
from Entity.IncidentType import IncidentType

class MainModule:
    @staticmethod
    def main():
        # Create an instance of CrimeAnalysisServiceImpl
        service_impl = CrimeAnalysisServiceImpl()

        # Create an incident
        incident = Incident(incident_id=7, incident_type="Type 7", incident_date="2024-01-01", location="Location 7",
                            description="Incident 7 Description", status="Open", victim_id=7, suspect_id=7)

        # Call createIncident method
        success = service_impl.createIncident(incident)
        print("Incident creation success:", success)

        # Update incident status
        success = service_impl.updateIncidentStatus(status="Closed", incident_id=1)
        print("Incident status update success:", success)

        # Get incidents in a date range
        incidents = service_impl.getIncidentsInDateRange("2024-01-01", "2024-01-31")
        print("Incidents in date range:", incidents)

        # Search for incidents based on criteria
        criteria = IncidentType(type_id=1, type_name="Type 1")
        searched_incidents = service_impl.searchIncidents(criteria)
        print("Searched incidents:", searched_incidents)

        # Generate incident report
        report = service_impl.generateIncidentReport(incident)
        print("Generated report:", report)

        # Create a case
        case_id = service_impl.createCase("Case 1 Description", [1, 2, 3])
        print("Created case ID:", case_id)

        # Get case details
        case_details = service_impl.getCaseDetails(case_id)
        print("Case details:", case_details)

        # Update case details
        success = service_impl.updateCaseDetails(case_id, "Updated Case Description")
        print("Case details update success:", success)

        # Get all cases
        all_cases = service_impl.getAllCases()
        print("All cases:", all_cases)

if __name__ == "__main__":
    MainModule.main()
