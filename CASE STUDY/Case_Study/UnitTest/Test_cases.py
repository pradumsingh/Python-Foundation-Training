import unittest
from Entity.Incidents import Incidents

class TestIncidents(unittest.TestCase):
    def setUp(self):
        self.incident = Incidents()

    def test_create_incident(self):
        """Test if an incident is created successfully"""
        print("Creating a new incident with incident id = 5")
        result = self.incident.insert_into()
        self.assertEqual('Incident created successfully', result, "Failed to create incident with ID 5")

    def test_update_incident_status(self):
        """Test if incident status is updated successfully"""
        print("Updating the status of incident. Set status = Investigation")
        result = self.incident.update_table()
        self.assertEqual('Values updated successfully', result, "Failed to update incident status to 'Investigation'")

if __name__ == '__main__':
    unittest.main()
