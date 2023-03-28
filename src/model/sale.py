class sale:
    def __init__(self, quantity, date_conclusion, date_opening, sale_id, fk_client_id, fk_cashier_id,
                 fk_form_of_payment):
        self.quantity = quantity
        self.date_conclusion = date_conclusion
        self.date_opening = date_opening
        self.id = sale_id
        self.fk_client_id = fk_client_id
        self.fk_cashier_id = fk_cashier_id
        self.fk_form_of_payment = fk_form_of_payment
