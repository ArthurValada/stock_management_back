from datetime import datetime


class Sale:
    def __init__(self, quantity: int, date_opening: datetime, sale_id: int, fk_client_id: int,
                 fk_cashier_id: int, fk_form_of_payment: int, active: bool,
                 fks_products_ids: list[int] = None, date_conclusion: datetime = None):
        self.quantity: int = quantity
        self.date_conclusion: datetime = date_conclusion
        self.date_opening: datetime = date_opening
        self.id: int = sale_id
        self.fk_client_id: int = fk_client_id
        self.fk_cashier_id: int = fk_cashier_id
        self.fk_form_of_payment: int = fk_form_of_payment
        self.products_ids: list[int] = fks_products_ids
        self.active: bool = active
