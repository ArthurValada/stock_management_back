from datetime import datetime


class Cashier:
    def __init__(self, cashier_id: int, date_opening: datetime, fk_manager_open: int, fk_manager_closure: int,
                 date_closure: datetime = None):
        self.id: int = cashier_id
        self.date_opening: datetime = date_opening
        self.date_closure: datetime = date_closure
        self.fk_manager_open_id: int = fk_manager_open
        self.fk_manager_closure_id: int = fk_manager_closure
