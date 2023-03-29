import string


class product:

    def __init__(self, product_id: int, name: string, price: float, description: string, active: bool,
                 fk_employee_id: int):
        self.id: int = product_id
        self.name: string = name
        self.price: float = price
        self.description: string = description
        self.active: bool = active
        self.fk_employee_id: int = fk_employee_id

