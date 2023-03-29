import string


class contact:

    def __init__(self, contact_id: int, ddd: int, number: int, active: bool, email: string):
        self.id: int = contact_id
        self.ddd: int = ddd
        self.number: int = number
        self.email: string = email
        self.active: bool = active

