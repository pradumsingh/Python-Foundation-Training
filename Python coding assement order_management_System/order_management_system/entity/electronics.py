from product import Product

class Clothing(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, type, size, color):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.size = size
        self.color = color

    # Specific getters and setters for Clothing attributes
    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def set_size(self, newSize):
        self.size = newSize

    def set_color(self, newColor):
        self.color = newColor
