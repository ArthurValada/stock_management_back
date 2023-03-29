class Local:

    def __init__(self, local_id: int, description: str, fk_manager_id: int, is_active: bool):
        self.id: int = local_id
        self.description: str = description
        self.registered_by_employee_id: int = fk_manager_id
        self.is_active: bool = is_active
        