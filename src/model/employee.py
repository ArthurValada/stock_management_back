import src

# from datetime import datetime
# todo: datetime


class Employee(src.db.Model):
    # def __init__(self, employee_id: int, name: str, date_of_birth: str, sex: str, cpf: str, password: str,
    #              employee_type: int, is_active: bool, contacts_ids: list[int] = None, sales_made: list[int] = None):
    #     self.sales_made: list[int] = sales_made
    #     self.id: int = employee_id
    #     self.name: str = name
    #     self.date_of_birth: str = date_of_birth
    #     self.sex: str = sex
    #     self.cpf: str = cpf
    #     self.password: str = password
    #     self.type: int = employee_type
    #     self.contacts: list[int] = contacts_ids
    #     self.is_active: bool = is_active
    id = src.db.Column(src.db.Integer, primary_key=True, autoincrement=True)
    name = src.db.Column(src.db.String(50), nullable=False)
    is_active = src.db.Column(src.db.Boolean, nullable=False)
    date_of_birth = src.db.Column(src.db.Date)
    sex = src.db.Column(src.db.CHAR)
    cpf = src.db.Column(src.db.String(11))
    password = src.db.Column(src.db.String(20))
    # registers = src.db.relationship('model.product.Product', backref='register', lazy=True)
    # todo: employee type?
    # todo: contact
    # todo: sales made

    def __repr__(self):
        return f"Employee('{self.id}', '{self.name}', '{self.is_active}')"

    def serilizable(self):
        base_dict = self.__dict__
        base_dict.pop('_sa_instance_state')
        return base_dict
