class Product:

    def __init__(self, product_id: int, name: str, price: float, description: str, active: bool,
                 fk_registered_by_employee_id: int, fk_batch_id: list(int) = None, fk_supplier_id: list(int) = None):
        self.id: int = product_id
        self.name: str = name
        self.price: float = price
        self.description: str = description
        self.active: bool = active
        self.fk_registered_by_employee_id: int = fk_registered_by_employee_id
        self.is_in_batch_id: list(int) = fk_batch_id
        self.provided_by_supplier_id: list(int) = fk_supplier_id

