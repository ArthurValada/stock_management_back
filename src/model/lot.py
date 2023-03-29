from datetime import datetime


class Lot:

    def __init__(self, lot_id: int, purchase_price: float, quantity: int, active: bool, fk_supplier_id: int,
                 expiration_date: datetime = None):
        self.id: int = lot_id
        self.quantity: int = quantity
        self.purchase_price: float = purchase_price
        self.expiration_date: datetime = expiration_date
        self.supplied_by_supplier_id: int = fk_supplier_id
        self.active: bool = active

