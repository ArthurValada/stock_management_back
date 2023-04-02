from flask import abort, make_response


def login_name(name, password):
    # same_name = filter(lambda x: True if x.name == name else False, STORAGE.values())
    # if not same_name:
    #     abort(404, f'No employee named {name} found')
    #
    # for employee in same_name:
    #     if employee.password == password:
    #         return make_response(f'{name} succefully logged on!', 200)
    #
    # abort(401, "The given password doesn't match the given name")
    pass
