from datetime import datetime
import src


class Product(src.db.Model):
    id = src.db.Column(src.db.Integer, primary_key=True, autoincrement=True)
    name = src.db.Column(src.db.String(50), nullable=False)
    is_active = src.db.Column(src.db.Boolean, nullable=False)
    price = src.db.Column(src.db.Float, nullable=False)
    description = src.db.Column(src.db.String(280))
    register = src.db.Column(src.db.Integer, src.db.ForeignKey('employee.id'), nullable=False)
    registry_date = src.db.Column(src.db.DateTime, nullable=False, default=datetime.utcnow)
    # todo: batch_id
    # todo: supplier_id

    def __repr__(self):
        return f"Product('{self.id}', '{self.name}', '{self.price}', '{self.is_active}'"


def remove_args(kwargs: dict) -> dict:
    kwargs.pop('id', None)
    kwargs.pop('fk_batch', None)
    kwargs.pop('fk_supplier', None)
    if 'registry_date' in kwargs:
        kwargs['registry_date'] = datetime.strptime(kwargs['registry_date'], '%Y-%m-%d')
    return kwargs
