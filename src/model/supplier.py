import string


class supplier:

    def __init__(self, supplier_id: int, name: string, fk_employee_id: int):
        self.id: int = supplier_id
        self.name: string = name
        self.fk_employee_id: int = fk_employee_id

