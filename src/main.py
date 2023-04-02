from src import connexion_app, db
from src.model import *
# from datetime import datetime

if __name__ == '__main__':
    with connexion_app.app.app_context():
        # db.drop_all()
        # db.session.add(employee.Employee(name='nome', date_of_birth=datetime.utcnow(), sex='m',
        #                         cpf='2020202', password='senha', is_active=True))
        # db.session.commit()
        print(db.metadata.tables.keys())

    connexion_app.run(port=8001, debug=True)
