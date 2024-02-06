from DBUtil import DBUtil
from TechShopImpl import TechShopServiceImpl


class MyTechShop(TechShopServiceImpl):
    def __init__(self, dbUtil):
        super().__init__(dbUtil)

    def start(self):
        while True:
            print("Please select an option from the following:")
            print("1. Customer Registration")
            print("2. Update Product Information")
            print("3. Place New Order")
            print("4. Track Order Status")
            print("5. Manage Inventory")
            print("6. Sales Reporting")
            print("7. Customer Account Updates")
            print("8. Payment Processing")
            print("9. Product Search and Recommendations")
            print("10. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.customer_registration()
                print("Thank you for registering with us.")
                print("Returning to main menu.")
            elif choice == 2:
                self.update_product_info()
                print("Changes made successfully!")
                print("Returning to main menu.")
            elif choice == 3:
                self.place_order()
                print("Order placed successfully.")
                print("Returning to main menu.")
            elif choice == 4:
                self.track_order_status()
                print("Returning to main menu.")
            elif choice == 5:
                self.manage_inventory()
                print("Returning to main menu.")
            elif choice == 6:
                self.sales_reporting()
                print("Returning to main menu.")
            elif choice == 7:
                self.customer_account_updates()
                print("Updates were successful.")
                print("Returning to main menu.")
            elif choice == 8:
                self.payment_processing()
                print("Returning to main menu.")
            elif choice == 9:
                self.product_search_and_recommendations()
                print("Returning to main menu.")
            elif choice == 10:
                print("Thanks for visiting us. See you anytime soon.")
                break


dbutil = DBUtil()
my_tech_shop = MyTechShop(dbutil)
my_tech_shop.start()
