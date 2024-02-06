class InvalidDataException(Exception):
    def __init__(self, message):
        self.message = message


class MyCustomers:
    def __init__(self, customer_id: int, first_name: str, last_name: str, email: str, phone: str, address: str):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._address = address

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, cid):
        self._customer_id = cid

    @property
    def name(self):
        return f"{self._first_name} {self._last_name}"

    @name.setter
    def name(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        try:
            if '@' in email:
                self._email = email
            else:
                raise InvalidDataException("Invalid email")
        except InvalidDataException as idv:
            print("@ is missing in the input provided. ", idv)

    def calculate_total_orders(self):
        pass

    def get_customer_details(self):
        print("Customer ID:", self._customer_id)
        print("Customer Name:", self.name)
        print("Customer Email:", self._email)
        print("Customer Phone:", self._phone)
        print("Customer Address:", self._address)

    def update_customer_info(self, email):
        self._email = email
