from src import main

# from datetime import datetime
# todo: datetime


class Employee(main.db.Model):
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
    id = main.db.Column(main.db.Integer, primary_key=True, auto_increment=True)
    name = main.db.Column(main.db.String(50), nullable=False)
    is_active = main.db.Column(main.db.Boolean, nullable=False)
    date_of_birth = main.db.Column(main.db.Date)
    sex = main.db.Column(main.db.Char)
    cpf = main.db.Column(main.db.String(11))
    password = main.db.Column(main.db.String(20))
    registers = main.db.relationship('Product', backref='register', lazy=True)
    # todo: employee type?
    # todo: contact
    # todo: sales made

    def __repr__(self):
        return f"Employee('{self.id}', '{self.name}', '{self.is_active}')"
