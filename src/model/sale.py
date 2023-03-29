from datetime import datetime


class sale:
    def __init__(self, quantity: int, date_conclusion: datetime, date_opening: datetime, sale_id: int, fk_client_id: int,
                 fk_cashier_id: int, fk_form_of_payment: int):
        self.quantity: int = quantity
        self.date_conclusion: datetime = date_conclusion
        self.date_opening: datetime = date_opening
        self.id: int = sale_id
        self.fk_client_id: int = fk_client_id
        self.fk_cashier_id: int = fk_cashier_id
        self.fk_form_of_payment: int = fk_form_of_payment
