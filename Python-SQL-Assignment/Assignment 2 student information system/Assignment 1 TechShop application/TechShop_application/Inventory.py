import datetime
from Products import Products

class Inventory(Products):
    def __init__(self, inventory_id: int, product, quantity_in_stock: int, last_stock_update: int):
        self._inventory_id = inventory_id
        super().__init__(product.product_id, product.product_name, product.description, product.price)
        self._quantity_in_stock = quantity_in_stock
        self._last_stock_update = last_stock_update

    @property
    def quantity_in_stock(self):
        return self._quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, quantity):
        self._quantity_in_stock = quantity

    def get_product(self):
        print(f"Inventory ID: {self._inventory_id}")
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Product Description: {self.description}")
        print(f"Product Price: {self.price}")

    def add_to_inventory(self, quantity):
        self._quantity_in_stock += quantity

    def remove_from_inventory(self, quantity):
        try:
            if quantity <= self._quantity_in_stock:
                self._quantity_in_stock -= quantity
                self._last_stock_update = self._quantity_in_stock
            else:
                raise ValueError("Quantity is greater than available quantity.")
        except ValueError as e:
            print("Invalid quantity:", e)

    def update_stock_quantity(self, new_quantity):
        try:
            if new_quantity >= 0:
                self._quantity_in_stock += new_quantity
                self._last_stock_update = self._quantity_in_stock
            else:
                raise ValueError("Quantity cannot be negative.")
        except ValueError as e:
            print("Please enter a valid quantity:", e)

    def is_product_available(self, quantity):
        if quantity >= self._quantity_in_stock:
            print(f"Yes! The product {self.product_name} is available.")
        else:
            print("Sorry! The product is not available right now.")

    def list_low_stock_products(self, threshold):
        if self._quantity_in_stock < threshold:
            print(f"Low stock for {self.product_name}")
        else:
            print("The stock is available")

    def list_out_of_stock_products(self):
        pass

    def list_all_products(self):
        pass
