from datetime import datetime


class lot:

    def __init__(self, lot_id: int, purchase_price: float, quantity: int, expiration_date: datetime):
        self.id: int = lot_id
        self.quantity: int = quantity
        self.purchase_price: float = purchase_price
        self.expiration_date: datetime = expiration_date

