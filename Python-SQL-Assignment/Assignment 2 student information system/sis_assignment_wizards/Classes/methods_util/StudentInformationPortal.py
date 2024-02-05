from datetime import datetime

class WizardryStudentPortal:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_wizard_information(self):
        query = ("SELECT wizard_id, CONCAT(first_name, ' ', last_name) AS 'Name', date_of_birth, owl_email, broomstick_number "
                 "FROM wizards")
        result = self.db_connection.fetchall(query)
        return result

    def register_new_wizard(self):
        wizard_id = self.generate_unique_wizard_id()
        print("Fill up the wizard details:")
        wizard_info = {
            'wizard_id': wizard_id,
            'first_name': input("Enter the First Name: "),
            'last_name': input("Enter the Last Name: "),
            'date_of_birth': input("Enter the date of birth: "),
            'owl_email': input("Enter the Owl Email: "),
            'broomstick_number': input("Enter the Broomstick Number:")
        }
        if not self.check_owl_email(wizard_info['owl_email']):
            raise Exception("Owl Email already exists")
        if not self.check_broomstick_number(wizard_info['broomstick_number']):
            raise Exception("Broomstick Number already exists")

        query = "INSERT INTO wizards VALUES (%s, %s, %s, %s, %s, %s)"
        values = (wizard_info['wizard_id'], wizard_info['first_name'], wizard_info['last_name'],
                  wizard_info['date_of_birth'], wizard_info['owl_email'], wizard_info['broomstick_number'])
        return self.db_connection.execute_query(query, values)

    def enroll_wizard_in_course(self):
        enrollment_id = self.generate_unique_enrollment_id()
        enrollments = {
            'enrollment_id': enrollment_id,
            'wizard_id': input("Enter the wizard ID: "),
            'enrollment_date': datetime.now().strftime("%Y-%m-%d")
        }
        query = "INSERT INTO enrollments VALUES (%s, %s, %s, %s)"
        print("Choose which Course you want to enroll in:")
        print("1. Introduction to Wizardry")
        print("2. Potions 101")
        print("3. Spell Casting")
        print("4. Defense Against the Dark Arts")
        print("5. Magical Creatures Study")
        choice = int(input("Enter: "))
        if 1 <= choice <= 5:
            enrollments['course_id'] = f'C00{choice}'
            values = (enrollments['enrollment_id'], enrollments['wizard_id'], enrollments['course_id'],
                      enrollments['enrollment_date'])
            return self.db_connection.execute_query(query, values)
        else:
            print("Invalid choice. Enrollment aborted.")
            return None

    def get_no_of_wizards(self):
        query = "SELECT COUNT(*) FROM wizards"
        result = self.db_connection.fetch_one(query)
        return result[0]

    def get_no_of_enrollments(self):
        query = "SELECT COUNT(*) FROM enrollments"
        result = self.db_connection.fetch_one(query)
        return result[0]

    def generate_unique_wizard_id(self):
        return f'WZ{self.get_no_of_wizards() + 1:03d}'

    def generate_unique_enrollment_id(self):
        return f'EN{self.get_no_of_enrollments() + 1:03d}'

    def check_owl_email(self, owl_email):
        query = "SELECT owl_email FROM wizards"
        result = self.db_connection.fetchall(query)
        return owl_email not in result[0]

    def check_broomstick_number(self, broomstick_number):
        query = "SELECT broomstick_number FROM wizards"
        result = self.db_connection.fetchall(query)
        return broomstick_number not in result[0]
