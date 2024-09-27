import random
from datetime import datetime
from xmlrpc.client import DateTime


class Purchase:
    id: str
    product_id: str
    quantity: int
    timestamp: DateTime

    def __init__(self, id, product_id, quantity=None, timestamp=None):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity if quantity else random.randint(1, 100)
        self.timestamp = timestamp if timestamp else datetime.now()

    def __dict__(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'timestamp': self.timestamp.isoformat(),
        }
