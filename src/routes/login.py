from flask import abort, make_response
from src.model import employee as emp


def login_name(name, password):
    same_name = emp.Employee.query.filter_by(name=name)
    if not same_name:
        abort(404, f'No employee named {name} found')

    for employee in same_name:
        if employee.password == password:
            return make_response(f'{name} succefully logged on!', 200)

    abort(401, "The given password doesn't match the given name")
