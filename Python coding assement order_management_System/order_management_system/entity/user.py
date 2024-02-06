from product import Product  # Include this if users might also inherit product attributes

class User:
    def __init__(self, userId, username, password, role):
        self.userId = userId
        self.username = username
        self.password = password
        self.role = role

    def get_userId(self):
        return self.userId

    def get_username(self):
        return self.username

    def get_password(self):
        # Don't return the actual password for security reasons
        return "***"  # Placeholder

    def get_role(self):
        return self.role

    def set_userId(self, newUserId):
        self.userId = newUserId

    def set_username(self, newUsername):
        self.username = newUsername

    def set_password(self, newPassword):
        self.password = newPassword

    def set_role(self, newRole):
        self.role = newRole


# user1 = User(1, "admin", "password123", "Admin")
# print(f"User ID: {user1.get_userId()}")
# print(f"Username: {user1.get_username()}")
# print(f"Password: {user1.get_password()}")  # Prints "***"
# print(f"Role: {user1.get_role()}")