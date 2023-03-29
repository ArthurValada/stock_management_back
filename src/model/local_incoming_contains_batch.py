from datetime import datetime


class local_incoming_contains_batch:

    def __init__(self, fk_employee_id: int, fk_batch_id: int, fk_local_id: int,
                 active: bool, is_entry: bool, date: datetime):
        self.is_entry: bool = is_entry
        self.date: datetime = date
        self.active: bool = active
        self.fk_authorized_by_employee_id: int = fk_employee_id
        self.fk_local_id: int = fk_local_id
        self.fk_batch_id: int = fk_batch_id
