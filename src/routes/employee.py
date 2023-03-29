from flask import abort, make_response
from src.model.employee import Employee

# from datetime import datetime

from src.run import STORAGE  # todo: remove this


def id_not_found(item_id): abort(404, f'Employee with id {item_id} not found')


def read_all():
    return list(map(lambda i: i.__dict__, STORAGE.values()))


def read_one(item_id):
    if item_id in STORAGE:
        return STORAGE[item_id].__dict__
    else:
        id_not_found(item_id)


def create(employee):
    if len(STORAGE) > 0:
        new_id = list(STORAGE.keys())[-1] + 1
    else:
        new_id = 0

    new_employee = Employee(
        new_id,  # if the framework obligates to put some id, put it -1
        employee['name'],
        employee['date_of_birth'],
        employee['sex'],
        employee['cpf'],
        employee['password'],
        employee['type'],
        employee['is_active']
    )

    STORAGE[new_employee.id] = new_employee
    return new_employee.__dict__, 201


def update(item_id, employee):
    if item_id in STORAGE:
        new_employee = Employee(
            item_id,  # if the framework obligates to put some id, put it -1
            employee['name'],
            employee['date_of_birth'],
            employee['sex'],
            employee['cpf'],
            employee['password'],
            employee['employee_type']
        )
        STORAGE[new_employee.id] = new_employee
        return new_employee.__dict__
    else:
        id_not_found(item_id)


def delete(item_id):
    if item_id in STORAGE:
        del STORAGE[item_id]
        return make_response(f'Employee {item_id} successfully deleted', 200)
    else:
        id_not_found(item_id)
