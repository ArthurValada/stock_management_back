# from datetime import datetime
# todo: datetime

class Employee:

    def __init__(self, employee_id: int, name: str,
                 date_of_birth: str, sex: str, cpf: str,
                 password: str, employee_type: int):
        self.id: int = employee_id
        self.name: str = name
        self.date_of_birth: str = date_of_birth
        self.sex: str = sex
        self.cpf: str = cpf
        self.password: str = password
        self.type: int = employee_type
        