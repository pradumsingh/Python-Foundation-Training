class Products:
    def __init__(self, product_id: int, product_name, description, price: float):
        self._product_id = product_id
        self._product_name = product_name
        self._description = description
        self._price = price

    @property
    def product_id(self):
        return self._product_id

    @property
    def product_name(self):
        return self._product_name

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self._price

    @product_id.setter
    def product_id(self, pid):
        self._product_id = pid

    @product_name.setter
    def product_name(self, name):
        self._product_name = name

    @description.setter
    def description(self, desc):
        self._description = desc

    @price.setter
    def price(self, price):
        try:
            if price >= 0:
                self._price = price
            else:
                raise ValueError("Price cannot be negative")
        except ValueError as e:
            print("Price must be a non-negative value:", e)

    def get_product_details(self):
        print("Product ID:", self._product_id)
        print("Product Name:", self._product_name)
        print("Description:", self._description)
        print("Price:", self._price)

    def update_product_info(self, price):
        try:
            if price >= 0:
                self._price = price
            else:
                raise ValueError("Price cannot be negative")
        except ValueError as e:
            print("Please enter a valid price:", e)

    def is_product_in_stock(self):
        pass
