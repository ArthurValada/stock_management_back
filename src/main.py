from src import connexion_app, db

if __name__ == '__main__':
    with connexion_app.app.app_context():
        print(db.metadata.tables.keys())

    connexion_app.run(port=8001, debug=True)
