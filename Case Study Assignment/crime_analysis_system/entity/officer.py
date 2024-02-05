# entity/officer.py

class Officer:
    def __init__(self, officer_id, first_name, last_name, badge_number, rank, contact_info, agency_id):
        self.officer_id = officer_id
        self.first_name = first_name
        self.last_name = last_name
        self.badge_number = badge_number
        self.rank = rank
        self.contact_info = contact_info
        self.agency_id = agency_id
        self.reports = []  # Initialize reports as an empty list

    def add_report(self, report):
        self.reports.append(report)

    def get_officer_details(self):
        # Implement any details retrieval logic if needed
        pass

    def __str__(self):
        return f"OfficerID: {self.officer_id}, FirstName: {self.first_name}, LastName: {self.last_name}, BadgeNumber: {self.badge_number}, Rank: {self.rank}"

'''
# Generate instances for testing
if __name__ == "__main__":
    # Create multiple instances of Officer for testing
    officer1 = Officer(officer_id=1, first_name="John", last_name="Doe", badge_number="12345", rank="Sergeant", contact_info="789 Lane, City, Country", agency_id=1)
    officer2 = Officer(officer_id=2, first_name="Jane", last_name="Smith", badge_number="67890", rank="Detective", contact_info="456 Road, City, Country", agency_id=2)

    # Display officer details
    print(officer1)
    print(officer2)
'''