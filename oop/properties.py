"""properties"""

# getter and setter in python


# class Product:
#     """product class"""

#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         """Getter"""
#         return self.__price

#     def set_price(self, value):
#         """Setter"""
#         if value < 0:
#             raise ValueError('Price cannot be negative')
#         self.__price = value
#     price = property(get_price, set_price)


# product = Product(50)
# product.price = -1
# print(product.price)
class Product:
    """product class"""

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        """Getter"""
        return self.__price

    @price.setter
    def set_price(self, value):
        """Setter"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(50)
product.price = -1
print(product.price)
