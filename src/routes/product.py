from flask import abort, make_response
from src.model import product as prod
from src.utils.serialization import serial
from src import db


def id_not_found(item_id): abort(404, f'No product with id {item_id} found')


def read_all():
    items = list(map(lambda i: serial(i), prod.Product.query.all()))
    print('product.read_all():\n', items)
    return items, 200


def read_one(**kwargs):
    product = prod.Product.query.get(kwargs['id'])
    if product:
        return serial(product), 200
    else:
        id_not_found(kwargs['id'])


def create(**kwargs):
    product = prod.Product(**prod.remove_args(kwargs['product']))
    response = serial(product)
    db.session.add(product)
    db.session.commit()

    return response, 201


def update(**kwargs):
    product = prod.Product.query.get(kwargs['id'])
    if product:
        product_data = serial(product)
        product_data.update(prod.remove_args(kwargs['body']))

        db.session.delete(product)
        db.session.add(prod.Product(**product_data))
        db.session.commit()
        return product_data, 201
    else:
        id_not_found(kwargs['id'])


def delete(**kwargs):
    product = prod.Product.query.get(kwargs['id'])
    if product:
        db.session.delete(product)
        db.session.commit()
        return make_response(f"Product {kwargs['id']} successfully deleted", 200)
    else:
        id_not_found(kwargs['id'])

