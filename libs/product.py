import faker_commerce
from faker import Faker


class Product:
    id: str
    name: str
    price: float

    def __init__(self, id, name=None, price=None):
        fake = Faker()
        fake.add_provider(faker_commerce.Provider)
        self.id = id
        self.name = name if name else fake.ecommerce_name()
        self.price = price if price else round(fake.ecommerce_price() / 1000000, 2)

    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
        }
