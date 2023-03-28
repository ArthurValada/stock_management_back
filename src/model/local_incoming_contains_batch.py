class local_incoming_contains_batch:

    def __init__(self, fk_employee_id, fk_batch_id, fk_local_id, active, is_entry,date):
        self.is_entry = is_entry
        self.date = date
        self.fk_employee_id = fk_employee_id
        self.fk_local_id = fk_local_id
        self.active= active
        self.fk_batch_id = fk_batch_id
