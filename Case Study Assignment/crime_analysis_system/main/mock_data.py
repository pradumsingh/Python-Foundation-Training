from entity.victim import Victim
from entity.suspect import Suspect
from entity.law_enforcement_agency import LawEnforcementAgency
from entity.officer import Officer
from entity.evidence import Evidence
from entity.incident import Incident
from entity.report import Report

class MockDB:
    def __init__(self):
        self.victims = {}
        self.suspects = {}
        self.agencies = {}
        self.officers = {}
        self.evidences = {}
        self.incidents = {}
        self.reports = {}

    def execute_query(self, query, values=None):
        # For mock purposes, we won't use this method
        pass

    def fetch_query(self, query, values=None):
        # For mock purposes, we won't use this method
        pass

    def close_connection(self):
        # For mock purposes, we won't use this method
        pass

# Rest of your code...

# Create an instance of MockDB
mock_db = MockDB()

# Mock data creation
victim1 = Victim(1, 'Rajesh', 'Kumar', '1990-05-15', 'Male', 'Address: Delhi, Phone: 9876543210')
victim2 = Victim(2, 'Priya', 'Sharma', '1985-08-22', 'Female', 'Address: Mumbai, Phone: 8765432109')

suspect1 = Suspect(1, 'Amit', 'Singh', '1982-11-10', 'Male', 'Address: Kolkata, Phone: 7654321098')
suspect2 = Suspect(2, 'Neha', 'Patil', '1993-04-25', 'Female', 'Address: Bangalore, Phone: 6543210987')

agency1 = LawEnforcementAgency(1, 'Delhi Police', 'Delhi', 'Contact: 123-456-7890')
agency2 = LawEnforcementAgency(2, 'Mumbai Police', 'Mumbai', 'Contact: 987-654-3210')

officer1 = Officer(1, 'Vikram', 'Gupta', '123', 'Inspector', 'Contact: 234-567-8901', 1)
officer2 = Officer(2, 'Ananya', 'Rao', '456', 'Sergeant', 'Contact: 345-678-9012', 2)

evidence1 = Evidence(1, 'CCTV footage', 'Near the market', 1)
evidence2 = Evidence(2, 'Fingerprints', 'On the crime scene', 2)

incident1 = Incident(1, 'Robbery', '2023-01-05', 'POINT(28.6139 77.2090)', 'Theft at a jewelry store', 'Under Investigation', 1, 1)
incident2 = Incident(2, 'Homicide', '2023-02-10', 'POINT(19.0760 72.8777)', 'Murder in a residential area', 'Open', 2, 2)

report1 = Report(1, 1, 1, '2023-01-06', 'Initial investigation report', 'Draft')
report2 = Report(2, 2, 2, '2023-02-12', 'Preliminary findings', 'Finalized')

# Adding relationships between entities
victim1.incident = incident1
victim2.incident = incident2

suspect1.incident = incident1
suspect2.incident = incident2

agency1.officers = [officer1]
agency2.officers = [officer2]

officer1.reports = [report1]
officer2.reports = [report2]

incident1.evidences = [evidence1]
incident2.evidences = [evidence2, evidence1]  # incident2 has two evidences
incident1.reports = [report1]
incident2.reports = [report2]

# Adding entities to mock_db
mock_db.victims[victim1.get_victim_id()] = victim1
mock_db.victims[victim2.get_victim_id()] = victim2

mock_db.suspects[suspect1.get_suspect_id()] = suspect1
mock_db.suspects[suspect2.get_suspect_id()] = suspect2

mock_db.agencies[agency1.get_agency_id()] = agency1
mock_db.agencies[agency2.get_agency_id()] = agency2

mock_db.officers[officer1.get_officer_id()] = officer1
mock_db.officers[officer2.get_officer_id()] = officer2

mock_db.evidences[evidence1.get_evidence_id()] = evidence1
mock_db.evidences[evidence2.get_evidence_id()] = evidence2

mock_db.incidents[incident1.get_incident_id()] = incident1
mock_db.incidents[incident2.get_incident_id()] = incident2

mock_db.reports[report1.get_report_id()] = report1
mock_db.reports[report2.get_report_id()] = report2

# Print the mock data
print("Mock Victims:")
for victim_id, victim in mock_db.victims.items():
    print(victim)

print("\nMock Suspects:")
for suspect_id, suspect in mock_db.suspects.items():
    print(suspect)

# Print the mock data (continued)
print("\nMock Law Enforcement Agencies:")
for agency_id, agency in mock_db.agencies.items():
    print(agency)

print("\nMock Officers:")
for officer_id, officer in mock_db.officers.items():
    print(officer)

print("\nMock Evidence:")
for evidence_id, evidence in mock_db.evidences.items():
    print(evidence)

print("\nMock Incidents:")
for incident_id, incident in mock_db.incidents.items():
    print(incident)

print("\nMock Reports:")
for report_id, report in mock_db.reports.items():
    print(report)
