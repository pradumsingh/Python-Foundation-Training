from abc import ABC, abstractmethod
from i_order_management_repository import IOrderManagementRepository  # Assuming the interface file is in the same directory
from entity.product import Product
from entity.user import User


class OrderProcessor(IOrderManagementRepository):
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def create_order(self, user, products):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("INSERT INTO orders (user_id, products) VALUES (%s, %s)", (user.id, products))
            self.db_conn.commit()
            return True
        finally:
            cursor.close()

    def cancel_order(self, user_id, order_id):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("UPDATE orders SET status = 'canceled' WHERE user_id = %s AND id = %s", (user_id, order_id))
            self.db_conn.commit()
            return True
        finally:
            cursor.close()

    def create_product(self, user, product):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("INSERT INTO products (product_name, description, price) VALUES (%s, %s, %s)",
                           (product.product_name, product.description, product.price))
            self.db_conn.commit()
            return True
        finally:
            cursor.close()

    def create_user(self, user):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                           (user.username, user.password, user.role))
            self.db_conn.commit()
            return True
        finally:
            cursor.close()

    def get_all_products(self):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            return [Product(*product) for product in products]
        finally:
            cursor.close()

    def get_orders_by_user(self, user):
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT * FROM orders WHERE user_id = %s", (user.id,))
            orders = cursor.fetchall()
            return orders
        finally:
            cursor.close()
