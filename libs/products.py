import random
from .product import Product


class Products:
    products = []

    def __init__(self, products_quantity):
        self.products = [Product(i) for i in range(products_quantity)]

    def __dict__(self):
        return [
            product.__dict__() for product in self.products
        ]

    def get_random_product(self):
        return random.choice(self.products)
