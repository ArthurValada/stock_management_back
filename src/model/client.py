import string
from datetime import datetime


class client:

    def __init__(self, client_id: int, cpf: string, name: string, sex: string, date_of_birth: datetime):
        self.id: int = client_id
        self.cpf: string = cpf
        self.name: string = name
        self.sex: string = sex
        self.date_of_birth: datetime = date_of_birth
        