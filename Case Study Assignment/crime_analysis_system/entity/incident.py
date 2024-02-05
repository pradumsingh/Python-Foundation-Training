# entity/incident.py

from .evidence import Evidence
class Incident:
    def __init__(self, incident_id=None, incident_type=None, incident_date=None, location=None, description=None,
                 status=None, victim_id=None, suspect_id=None):
        self.incident_id = incident_id
        self.incident_type = incident_type
        self.incident_date = incident_date
        self.location = location
        self.description = description
        self.status = status
        self.victim_id = victim_id
        self.suspect_id = suspect_id
        self.evidences = []  # Initialize evidences as an empty list

    def add_evidence(self, evidence):
        self.evidences.append(evidence)

    def add_report(self, report):
        # Add any logic needed for adding reports
        pass

    def get_incident_details(self):
        # Implement any details retrieval logic if needed
        pass

    def __str__(self):
        return f"IncidentID: {self.incident_id}, IncidentType: {self.incident_type}, ..."
'''
# Testing instances
# Testing instances
if __name__ == "__main__":
    # Create an incident instance
    sample_incident = Incident(
        incident_id=1,
        incident_type="Robbery",
        incident_date="2024-02-05",
        location="Latitude: 40.7128, Longitude: -74.0060",
        description="A robbery occurred at a local store.",
        status="Open",
        victim_id=101,
        suspect_id=201
    )

    # Add an evidence instance
    sample_evidence = Evidence(evidence_id=1, description="Security camera footage", location_found="Store premises", incident_id=sample_incident.incident_id)
    sample_incident.add_evidence(sample_evidence)

    # Display incident details
    print(sample_incident)
'''
