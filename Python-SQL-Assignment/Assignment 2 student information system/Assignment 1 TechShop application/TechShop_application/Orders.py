import datetime
from Customers import Customers


class Orders(Customers):
    def __init__(self, order_id: int, customer, order_date: datetime, total_amount: float):
        self._order_id = order_id
        super().__init__(customer.customerID, customer.firstName, customer.lastName, customer.email, customer.phone, customer.address)
        self._order_date = datetime.datetime.strptime(order_date, "%Y-%m-%d").date()
        self._total_amount = total_amount
        self._status = "Processing"

    @property
    def order_id(self):
        return self._order_id

    @property
    def order_date(self):
        return self._order_date

    @property
    def total_amount(self):
        return self._total_amount

    @property
    def status(self):
        return self._status

    @order_id.setter
    def order_id(self, oid):
        self._order_id = oid

    @order_date.setter
    def order_date(self, date):
        d = datetime.datetime.strptime(date, "%Y-%m-%d")
        self._order_date = d

    @total_amount.setter
    def total_amount(self, amount):
        try:
            if amount >= 0:
                self._total_amount = amount
            else:
                raise ValueError("Amount cannot be negative")
        except ValueError as v:
            print("Please enter a valid amount:", v)

    @status.setter
    def status(self, status):
        self._status = status

    def calculate_total_amount(self):
        return self._total_amount

    def update_order_status(self, status):
        self._status = status

    def cancel_order(self):
        pass

    def get_customer_name(self):
        print(self.customer.customerName)
