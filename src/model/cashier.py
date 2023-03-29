from datetime import datetime


class cashier:
    def __init__(self, cashier_id: int, date_opening: datetime, date_closure: datetime):
        self.id: int = cashier_id
        self.date_opening: datetime = date_opening
        self.date_closure: datetime = date_closure

