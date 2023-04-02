from flask import abort, make_response
from src.model import employee as emp
from src.utils.serialization import serial
from src import db

# todo: catch excepions


def id_not_found(item_id): abort(404, f'No employee with id {item_id} found')


def read_all():
    items = list(map(lambda i: serial(i), emp.Employee.query.all()))
    print('employee.read_all():\n', items)
    return items, 200


def read_one(**kwargs):
    employee = emp.Employee.query.get(kwargs['id'])
    if employee:
        return serial(employee), 200
    else:
        id_not_found(kwargs['id'])


def create(**kwargs):
    employee = emp.Employee(**emp.remove_args(kwargs['employee']))
    response = serial(employee)
    db.session.add(employee)
    db.session.commit()

    return response, 201


def update(**kwargs):
    employee = emp.Employee.query.get(kwargs['id'])
    if employee:
        employee_data = serial(employee)
        employee_data.update(emp.remove_args(kwargs['body']))

        db.session.delete(employee)
        db.session.add(emp.Employee(**employee_data))
        db.session.commit()
        return employee_data, 201
    else:
        id_not_found(kwargs['id'])


def delete(**kwargs):
    employee = emp.Employee.query.get(kwargs['id'])
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return make_response(f"Employee {kwargs['id']} successfully deleted", 200)
    else:
        id_not_found(kwargs['id'])
