from flask import abort, make_response
from src.model import employee as emp


def login_id(id, password):
    same_id = emp.Employee.query.filter_by(id=id).all()
    if not same_id:
        abort(404, f'No employee with id {id} found')

    for employee in same_id:
        if employee.password == password:
            return make_response(f'{id} succefully logged on!', 200)

    abort(401, "The given password doesn't match the given name")
