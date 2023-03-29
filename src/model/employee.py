from datetime import datetime


class Employee:

    def __init__(self, employee_id: int, name: str, date_of_birth: datetime, sex: str, cpf: str, password: str,
                 employee_type: int, is_active: bool, contacts_ids: list(int) = None, sales_makes: list(int) = None):
        self.sales_makes: list(int) = sales_makes
        self.id: int = employee_id
        self.name: str = name
        self.date_of_birth: datetime = date_of_birth
        self.sex: str = sex
        self.cpf: str = cpf
        self.password: str = password
        self.type: int = employee_type
        self.contacts: list(int) = contacts_ids
        self.is_active: bool = is_active
