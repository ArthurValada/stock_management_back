class product:

    def __init__(self, product_id, name, price, description, active, fk_employee_id):
        self.id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.active = active
        self.fk_employee_id = fk_employee_id
