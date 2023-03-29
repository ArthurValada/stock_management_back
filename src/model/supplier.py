class Supplier:

    def __init__(self, supplier_id: int, name: str, fk_employee_id: int, contact_ids: list(int),active: bool,
                 fks_batchs_ids: list(int) = None):
        self.id: int = supplier_id
        self.name: str = name
        self.fk_registered_by_employee_id: int = fk_employee_id
        self.contacts: list(int) = contact_ids
        self.provider_batchs_ids: list(int) = fks_batchs_ids
        self.active: bool = active

