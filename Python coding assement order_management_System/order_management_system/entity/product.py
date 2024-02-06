class Product:
    def __init__(self, productId, productName, description, price, quantityInStock, type):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type

    def get_productId(self):
        return self.productId

    def get_productName(self):
        return self.productName

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_quantityInStock(self):
        return self.quantityInStock

    def get_type(self):
        return self.type

    def set_productId(self, newProductId):
        self.productId = newProductId

    def set_productName(self, newProductName):
        self.productName = newProductName

    def set_description(self, newDescription):
        self.description = newDescription

    def set_price(self, newPrice):
        self.price = newPrice

    def set_quantityInStock(self, newQuantityInStock):
        self.quantityInStock = newQuantityInStock

    def set_type(self, newType):
        self.type = newType
