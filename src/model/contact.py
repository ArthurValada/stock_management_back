class Contact:

    def __init__(self, contact_id: int, active: bool, ddd: int = None, number: int = None,
                 email: str = None):
        self.id: int = contact_id
        self.ddd: int = ddd
        self.number: int = number
        self.email: str = email
        self.active: bool = active
