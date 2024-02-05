# tests/test_crime_analysis_service.py
import unittest
from dao.crime_analysis_service_impl import CrimeAnalysisServiceImpl
from entity.incident import Incident
from exception import incident_number_not_found_exception

class TestCrimeAnalysisService(unittest.TestCase):

    def setUp(self):
        # Create a CrimeAnalysisServiceImpl instance
        self.crime_analysis_service = CrimeAnalysisServiceImpl()

    def test_create_incident(self):
        # Test incident creation
        new_incident = Incident(
            incident_type="Robbery",
            incident_date="2024-02-05",
            location="Location",
            description="Description",
            status="Open",
            victim_id=101,
            suspect_id=201
        )

        success = self.crime_analysis_service.create_incident(new_incident)

        # Check if the incident is created successfully
        self.assertTrue(success)

        # Check if the incident attributes are accurate
        self.assertEqual("Robbery", new_incident.incident_type)
        self.assertEqual("2024-02-05", new_incident.incident_date)
        self.assertEqual("Location", new_incident.location)
        self.assertEqual("Description", new_incident.description)
        self.assertEqual("Open", new_incident.status)
        self.assertEqual(101, new_incident.victim_id)
        self.assertEqual(201, new_incident.suspect_id)

    def test_update_incident_status(self):
        # Create a sample incident
        incident = Incident(
            incident_id=1,
            incident_type="Robbery",
            incident_date="2024-02-05",
            location="Location",
            description="Description",
            status="Open",
            victim_id=101,
            suspect_id=201
        )

        # Test incident status update
        success = self.crime_analysis_service.update_incident_status("Closed", incident)

        # Check if the status is updated successfully
        self.assertTrue(success)

        # Check if the incident's status is updated correctly
        self.assertEqual("Closed", incident.status)

    def test_invalid_status_update(self):
        # Create a sample incident
        incident = Incident(
            incident_id=1,
            incident_type="Robbery",
            incident_date="2024-02-05",
            location="Location",
            description="Description",
            status="Open",
            victim_id=101,
            suspect_id=201
        )

        # Test invalid incident status update
        with self.assertRaises(IncidentNumberNotFoundException):
            self.crime_analysis_service.update_incident_status("InvalidStatus", incident)

if __name__ == '__main__':
    unittest.main()
