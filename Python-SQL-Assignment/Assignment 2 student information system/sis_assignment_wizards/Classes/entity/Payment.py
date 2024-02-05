from Student import Student


class Payment(Student):
    def __init__(self, payment_id: int, student: Student, amount: float, payment_date: str):
        # Inherit student details from the parent Student class
        super().__init__(student.student_id, student.first_name, student.last_name, student.date_of_birth,
                         student.email_address, student.phone_number)
        self.payment_id = payment_id  # Unique payment identifier
        self.amount = amount  # Payment amount
        self.payment_date = payment_date  # Date of payment

    def get_payment_details(self):
        # Display Payment details
        print("Payment Details:")
        print(f"Payment ID: {self.payment_id}")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.first_name} {self.last_name}")
        print(f"Amount: {self.amount}")
        print(f"Date: {self.payment_date}")

# Uncomment the following code to test the Payment class with Harry Potter details
# if __name__ == '__main__':
#     harry_potter = Student(1, "Harry", "Potter", "31-07-1980", "harry@hogwarts.com", "123456789")
#     payment_for_harry = Payment(1, harry_potter, 500, "20-01-2024")
#
#     payment_for_harry.get_payment_details()
