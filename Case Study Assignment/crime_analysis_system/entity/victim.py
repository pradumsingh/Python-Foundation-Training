# entity/victim.py

class Victim:
    def __init__(self, victim_id, first_name, last_name, date_of_birth, gender, contact_information):
        self.victim_id = victim_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.contact_information = contact_information
        self.incidents = []  # Initialize incidents as an empty list

    def add_incident(self, incident):
        self.incidents.append(incident)

    def get_victim_details(self):
        # Implement any details retrieval logic if needed
        pass

    def __str__(self):
        return f"Victim(ID: {self.victim_id}, Name: {self.first_name} {self.last_name})"

'''
# Generate instances for testing
if __name__ == "__main__":
    # Create multiple instances of Victim for testing
    victim1 = Victim(victim_id=1, first_name="Alice", last_name="Smith", date_of_birth="1985-05-15", gender="Female", contact_information="123 Street, City, Country")
    victim2 = Victim(victim_id=2, first_name="Bob", last_name="Jones", date_of_birth="1990-08-22", gender="Male", contact_information="456 Avenue, City, Country")

    # Display victim details
    print(victim1)
    print(victim2)
'''