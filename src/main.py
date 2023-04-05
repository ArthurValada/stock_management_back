from src import connexion_app, db
from datetime import datetime

if __name__ == '__main__':
    with connexion_app.app.app_context():
        from src import employee

        db.session.add(employee.Employee(id=1, name="Sla", is_active=True, date_of_birth=datetime.utcnow().date(),
                                         sex="M", cpf="00000000000", password="password"))
        print(db.metadata.tables.keys())

    connexion_app.run(port=8001, debug=True)
