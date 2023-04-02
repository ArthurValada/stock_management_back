import src
from datetime import datetime


class Employee(src.db.Model):
    id = src.db.Column(src.db.Integer, primary_key=True, autoincrement=True)
    name = src.db.Column(src.db.String(50), nullable=False)
    is_active = src.db.Column(src.db.Boolean, nullable=False)
    date_of_birth = src.db.Column(src.db.Date)
    sex = src.db.Column(src.db.CHAR)
    cpf = src.db.Column(src.db.String(11))
    password = src.db.Column(src.db.String(20))
    registers = src.db.relationship('model.product.Product', backref='employee_register', lazy=True)
    # todo: employee type?
    # todo: contact
    # todo: sales made

    def __repr__(self):
        return f"Employee('{self.id}', '{self.name}', '{self.is_active}')"


def remove_args(kwargs: dict) -> dict:
    kwargs.pop('id', None)
    kwargs.pop('sales_made', None)
    kwargs.pop('contacts_id', None)
    kwargs.pop('employee_type', None)
    if 'date_of_birth' in kwargs:
        kwargs['date_of_birth'] = datetime.strptime(kwargs['date_of_birth'], '%Y-%m-%d').date()
    return kwargs
