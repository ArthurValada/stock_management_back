import string
from datetime import datetime
class employee:

    def __init__(self, employee_id: int, name: string, date_of_birth: datetime, sex: string, cpf: string, password: string, type: int):
        self.id: int = employee_id
        self.name: string = name
        self.date_of_birth: datetime = date_of_birth
        self.sex: string = sex
        self.cpf: string = cpf
        self.password: string = password
        self.type: int = type
        