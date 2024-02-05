# entity/law_enforcement_agency.py

class LawEnforcementAgency:
    def __init__(self, agency_id, agency_name, jurisdiction, contact_information, officers=None):
        self.agency_id = agency_id
        self.agency_name = agency_name
        self.jurisdiction = jurisdiction
        self.contact_information = contact_information
        self.officers = officers if officers is not None else []  # Initialize officers as an empty list if not provided

    def add_officer(self, officer):
        self.officers.append(officer)

    def __str__(self):
        return f"LawEnforcementAgency(ID: {self.agency_id}, Name: {self.agency_name}, Jurisdiction: {self.jurisdiction})"

'''
# Generate instances for testing
if __name__ == "__main__":
    # Create multiple instances of LawEnforcementAgency for testing
    agency1 = LawEnforcementAgency(agency_id=1, agency_name="City Police Department", jurisdiction="City", contact_information="123 Avenue, City, Country")
    agency2 = LawEnforcementAgency(agency_id=2, agency_name="County Sheriff's Office", jurisdiction="County", contact_information="456 Street, City, Country")

    # Display agency details
    print(agency1)
    print(agency2)
'''