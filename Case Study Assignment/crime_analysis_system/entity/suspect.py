# entity/suspect.py

class Suspect:
    def __init__(self, suspect_id, first_name, last_name, date_of_birth, gender, contact_information):
        self.suspect_id = suspect_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.contact_information = contact_information
        self.incidents = []  # Initialize incidents as an empty list

    def add_incident(self, incident):
        self.incidents.append(incident)

    def get_suspect_details(self):
        # Implement any details retrieval logic if needed
        pass

    def __str__(self):
        return f"Suspect(ID: {self.suspect_id}, Name: {self.first_name} {self.last_name})"

'''
# Generate instances for testing
if __name__ == "__main__":
    # Create multiple instances of Suspect for testing
    suspect1 = Suspect(suspect_id=1, first_name="John", last_name="Doe", date_of_birth="1980-03-10", gender="Male", contact_information="789 Lane, City, Country")
    suspect2 = Suspect(suspect_id=2, first_name="Jane", last_name="Smith", date_of_birth="1995-11-28", gender="Female", contact_information="456 Road, City, Country")

    # Display suspect details
    print(suspect1)
    print(suspect2)
'''