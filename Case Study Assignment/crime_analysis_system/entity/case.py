# case.py

class Case:
    def __init__(self, case_id, case_description, incidents):
        self.case_id = case_id
        self.case_description = case_description
        self.incidents = incidents

    def __str__(self):
        return f"CaseID: {self.case_id}, CaseDescription: {self.case_description}, Incidents: {self.incidents}"
