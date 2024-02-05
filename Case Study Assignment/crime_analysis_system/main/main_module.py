# main/main_module.py
from dao.crime_analysis_service_impl import CrimeAnalysisServiceImpl
from entity.incident import Incident
from exception import incident_number_not_found_exception

class MainModule:
    @staticmethod
    def main():
        # Create an instance of the service implementation
        crime_analysis_service = CrimeAnalysisServiceImpl()

        # Create an incident
        # Create an incident without specifying incident_id
        # Create an incident without specifying incident_id
        new_incident = Incident(
            incident_type="Robbery",
            incident_date="2024-02-05",
            location="Latitude: 40.7128, Longitude: -74.0060",
            description="A robbery occurred at a local store.",
            status="Open",
            victim_id=101,
            suspect_id=201
        )

        # Create incident in the database
        success = crime_analysis_service.create_incident(new_incident)
        print(f"Incident created successfully: {success}")

        # Update incident status
        incident_id_to_update = 1
        new_status = "Closed"
        success = crime_analysis_service.update_incident_status(new_status, incident_id_to_update)
        print(f"Incident status updated successfully: {success}")

        # Get incidents within a date range
        start_date = "2024-01-01"
        end_date = "2024-12-31"
        incidents_in_date_range = crime_analysis_service.get_incidents_in_date_range(start_date, end_date)
        print("Incidents within date range:")
        for incident in incidents_in_date_range:
            print(incident)

        # Get incident details by incident number
        incident_number_to_get_details = 1
        try:
            incident_details = crime_analysis_service.get_incident_details(incident_number_to_get_details)
            print("Incident details:")
            print(incident_details)
        except incident_number_not_found_exception as e:
            print(f"Exception: {e}")

# Run the main method when the script is executed
if __name__ == "__main__":
    MainModule.main()
