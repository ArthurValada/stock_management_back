class PaymentForm:

    def __init__(self, payment_form_id: int, description: str, active: bool):
        self.id: int = payment_form_id
        self.description: str = description
        self.active: bool = active
