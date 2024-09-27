import json
import time

from confluent_kafka import Producer

from libs import Products, Purchase


class DataGenerator:
    products = Products
    purchase_pause = 0
    purchase_counter = 0
    producer = Producer({
        "bootstrap.servers": "broker:9092"
    })

    def __init__(self, products_quantity, purchase_pause):
        self.products = Products(products_quantity)
        self.purchase_pause = purchase_pause

    def generate(self):
        [
            self.producer.produce(
                'products',
                json.dumps(product.__dict__())
            ) for product in self.products.products
        ]
        while True:
            self.purchase_counter += 1
            purchase = Purchase(
                self.purchase_counter,
                self.products.get_random_product().id,
            )

            self.producer.produce('purchases', json.dumps(purchase.__dict__()))
            print(
                json.dumps(
                    purchase.__dict__()
                )
            )
            time.sleep(self.purchase_pause)
