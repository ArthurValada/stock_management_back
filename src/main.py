import connexion
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import pathlib

basedir = pathlib.Path(__file__).parent.resolve()
connexion_app = connexion.App(__name__, specification_dir=basedir)

app = connexion_app.app

sqlite_db_path = 'main_sqlite.db'
sqlite3.connect(sqlite_db_path)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + sqlite_db_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# connexion_app.create_app().app_context().push()
db = SQLAlchemy(app)

connexion_app.add_api('swagger.yml')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    connexion_app.run(port=8001, debug=True)
