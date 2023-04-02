from datetime import datetime
import src


class Product(src.db.Model):
    # def __init__(self, product_id: int, name: str, price: float,
    #              description: str, active: bool, fk_registered_by_employee_id: int,
    #              fk_batch_id: list[int] = None, fk_supplier_id: list[int] = None):
    #     self.id: int = product_id
    #     self.name: str = name
    #     self.price: float = price
    #     self.description: str = description
    #     self.active: bool = active
    #     self.fk_registered_by_employee_id: int = fk_registered_by_employee_id
    #     self.is_in_batch_id: list[int] = fk_batch_id
    #     self.provided_by_supplier_id: list[int] = fk_supplier_id
    id = src.db.Column(src.db.Integer, primary_key=True, autoincrement=True)
    name = src.db.Column(src.db.String(50), nullable=False)
    is_active = src.db.Column(src.db.Boolean, nullable=False)
    price = src.db.Column(src.db.Float, nullable=False)
    description = src.db.Column(src.db.String(280))
    register = src.db.Column(src.db.Integer, src.db.ForeignKey('employee.id'), nullable=False)
    registry_date = src.db.Column(src.db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Product('{self.id}', '{self.name}', '{self.price}', '{self.is_active}'"
