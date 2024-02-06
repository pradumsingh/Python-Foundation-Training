import DBUtil
from order_processor import OrderProcessor

class OrderManagement:
    """Main class for user interaction and order management."""

    def __init__(self):
        self.db_util = DBUtil.DBUtil()
        self.processor = OrderProcessor(self.db_util)  # Create OrderProcessor using the same DBUtil instance

    def main(self):
        while True:
            print("\nOrder Management System")
            print("1. Create User")
            print("2. Create Product")
            print("3. Cancel Order")
            print("4. Get All Products")
            print("5. Get Order By User")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_user()
            elif choice == "2":
                self.create_product()
            elif choice == "3":
                self.cancel_order()
            elif choice == "4":

                self.get_all_products()
            elif choice == "5":
                self.get_order_by_user()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    def create_user(self):
        # Get user details
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (admin/user): ")

        # Call OrderProcessor method to create user
        try:
            user = self.processor.create_user(username, password, role)
            print("User created successfully:", user)
        except Exception as e:
            print("Error creating user:", e)

    def create_product(self):
        # Get product details
        product_name = input("Enter product name: ")
        description = input("Enter description: ")
        price = float(input("Enter price: "))

        # Call OrderProcessor method to create product
        try:
            product = self.processor.create_product(product_name, description, price)
            print("Product created successfully:", product)
        except Exception as e:
            print("Error creating product:", e)

    # ... (implement other methods similarly)

    def cancel_order(self):
        # Get order details
        user_id = int(input("Enter user ID: "))
        order_id = int(input("Enter order ID: "))

        # Call OrderProcessor method to cancel order
        try:
            self.processor.cancel_order(user_id, order_id)
            print("Order cancelled successfully.")
        except Exception as e:
            print("Error cancelling order:", e)

    def get_all_products(self):
        # Call OrderProcessor method to get all products
        products = self.processor.get_all_products()

        if products:
            print("\nProducts:")
            for product in products:
                print(product)  # Assuming product has a __str__ method
        else:
            print("No products found.")

    def get_order_by_user(self):
        # Get user details
        user_id = int(input("Enter user ID: "))

        # Call OrderProcessor method to get orders by user
        orders = self.processor.get_orders_by_user(user_id)

        if orders:
            print("\nOrders:")
            for order in orders:
                print(order)  # Assuming order has a __str__ method
        else:
            print("No orders found for this user.")

if __name__ == "__main__":
    order_system = OrderManagement()
    order_system.main()


