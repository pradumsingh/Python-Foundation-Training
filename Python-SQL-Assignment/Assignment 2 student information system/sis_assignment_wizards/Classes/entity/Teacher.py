class Teacher:
    def __init__(self, teacher_id: int, first_name: str, last_name: str, email: str):
        # Initialize Teacher attributes
        self.teacher_id = teacher_id  # Unique teacher identifier
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

#Uncomment the following code to test the Teacher class with Harry Potter details
if __name__ == '__main__':
   snape = Teacher(1, "Severus", "Snape", "snape@hogwarts.com")
   #Add more instances or test cases as needed
