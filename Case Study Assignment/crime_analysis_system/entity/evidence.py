# entity/evidence.py

class Evidence:
    def __init__(self, evidence_id, description, location_found, incident_id):
        self.evidence_id = evidence_id
        self.description = description
        self.location_found = location_found
        self.incident_id = incident_id

    def __str__(self):
        return f"EvidenceID: {self.evidence_id}, Description: {self.description}, LocationFound: {self.location_found}, IncidentID: {self.incident_id}"

'''
# Generate instances for testing
if __name__ == "__main__":
    # Create multiple instances of Evidence for testing
    evidence1 = Evidence(evidence_id=1, description="Security camera footage", location_found="Store premises", incident_id=1)
    evidence2 = Evidence(evidence_id=2, description="Fingerprint analysis", location_found="Crime scene", incident_id=2)

    # Display evidence details
    print(evidence1)
    print(evidence2)
'''