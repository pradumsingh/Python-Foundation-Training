from datetime import datetime

class WizardryPaymentService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_new_payment_record(self):
        payment_id = self.generate_unique_payment_id()
        print("Fill up the Magical Payment details:")
        payments = {
            'payment_id': payment_id,
            'wizard_id': input("Enter the Wizard ID: "),
            'amount': float(input("Enter the amount: ")),
            'payment_date': input("Enter the Payment Date in (YYYY-MM-DD) format: ")
        }
        query = "INSERT INTO magical_payments VALUES (%s, %s, %s, %s)"
        values = (payments['payment_id'], payments['wizard_id'], payments['amount'], payments['payment_date'])
        return self.db_connection.execute_query(query, values)

    def get_payment_details(self):
        wizard_id = input("Enter your Wizard ID: ")
        query = "SELECT * FROM magical_payments WHERE wizard_id = %s"
        values = (wizard_id,)
        result = self.db_connection.fetchall(query, values)
        return result

    def update_payment_records(self):
        payment_id = input("Enter your Payment ID: ")
        amount = input("Enter the amount")
        date = datetime.now().strftime("%Y-%m-%d")
        query = "UPDATE magical_payments SET amount=%s, payment_date=%s WHERE payment_id=%s"
        values = (amount, date, payment_id)
        return self.db_connection.execute_query(query, values)

    def get_no_of_payments(self):
        query = "SELECT COUNT(*) FROM magical_payments"
        result = self.db_connection.fetch_one(query)
        return result[0]

    def generate_unique_payment_id(self):
        return f'MP{self.get_no_of_payments() + 1:03d}'
