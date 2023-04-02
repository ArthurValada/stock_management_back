import connexion
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import pathlib

sqlite_db_path = 'main_sqlite.db'


basedir = pathlib.Path(__file__).parent.resolve()
connexion_app = connexion.App(__name__, specification_dir=basedir)
app = connexion_app.app

sqlite3.connect(sqlite_db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + sqlite_db_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

with app.app_context():
    from src.model import *
    db.create_all()

connexion_app.add_api('swagger.yml')


@app.route('/')
def home_route():
    return render_template('home.html')
