from datetime import datetime


class Client:

    def __init__(self, client_id: int, cpf: str, name: str, sex: str,
                 date_of_birth: datetime, is_active: bool, contacts_ids: list[int] = None):
        self.id: int = client_id
        self.cpf: str = cpf
        self.name: str = name
        self.sex: str = sex
        self.date_of_birth: datetime = date_of_birth
        self.contacts: list[int] = contacts_ids
        self.is_active: bool = is_active
        