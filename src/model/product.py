from datetime import datetime
from ..main import db


class Product(db.Model):
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
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(280))
    register = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    registry_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Product('{self.id}', '{self.name}', '{self.price}', '{self.is_active}'"
