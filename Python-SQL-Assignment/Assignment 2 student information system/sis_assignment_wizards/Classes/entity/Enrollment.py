from Student import Student
from Course import Course

class Enrollment:
    def __init__(self, enrollment_id: int, student: Student, course: Course, enrollment_date: str):
        # Initialize Enrollment attributes
        self.student = student  # Contains student information
        self.course = course    # Contains course information
        self.enrollment_id = enrollment_id  # Unique enrollment identifier
        self.enrollment_date = enrollment_date  # Date of enrollment

    def get_enrollment_details(self):
        # Display Enrollment details
        print("Enrollment Details:")
        print(f"Enrollment ID: {self.enrollment_id}")
        print(f"Student ID: {self.student.student_id}")
        print(f"Course ID: {self.course.course_id}")
        print(f"Enrollment Date: {self.enrollment_date}")

# Uncomment the following code to test the Enrollment class
# if __name__ == '__main__':
#     harry_potter = Student(1, "Harry", "Potter", "31-07-1980", "harry@hogwarts.com", "123456789")
#     potions_class = Course(2, "Potions", 101, "Professor Snape")
#     harry_enrollment = Enrollment(1, harry_potter, potions_class, "01-09-1991")
#
#     harry_enrollment.get_enrollment_details()
