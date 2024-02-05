# Create a file named 'exceptions.py' in your project
# exceptions.py
class IncidentNumberNotFoundException(Exception):
    def __init__(self, incident_number):
        self.incident_number = incident_number
        super().__init__(f"Incident with number {incident_number} not found.")
