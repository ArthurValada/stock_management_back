class manager_open_close_cashier:

    def __init__(self, fk_employee_id, fk_batch_id, opening_date, is_opening):
        self.fk_employee_id = fk_employee_id
        self.fk_batch_id = fk_batch_id
        self.opening_date = opening_date
        self.is_opening = is_opening

