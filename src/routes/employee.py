from flask import abort, make_response
from src.model import employee as emp
from src import db

STORAGE = {}


def id_not_found(item_id): abort(404, f'Employee with id {item_id} not found')


def read_all():
    print(list(map(lambda i: i.serilizable(), emp.Employee.query.all())))
    return list(map(lambda i: i.serilizable(), emp.Employee.query.all()))


def read_one(item_id):
    emp.Employee.query.filter()
    # else:
    #     id_not_found(item_id)


def create(employee):
    new_employee = emp.Employee(
        name=employee['name'],
        date_of_birth=employee['date_of_birth'],
        sex=employee['sex'],
        cpf=employee['cpf'],
        password=employee['password'],
        # employee['type'],
        is_active=employee['is_active']
    )

    return new_employee.__dict__, 201


def update(item_id, employee):
    if item_id in STORAGE:
        new_employee = emp.Employee(
            item_id,  # if the framework obligates to put some id, put it -1
            employee['name'],
            employee['date_of_birth'],
            employee['sex'],
            employee['cpf'],
            employee['password'],
            employee['employee_type'],
            employee['is_active']
        )
        STORAGE[new_employee.id] = new_employee
        return new_employee.__dict__, 201
    else:
        id_not_found(item_id)


def delete(item_id):
    if item_id in STORAGE:
        del STORAGE[item_id]
        return make_response(f'Employee {item_id} successfully deleted', 200)
    else:
        id_not_found(item_id)
