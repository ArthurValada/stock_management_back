from flask import render_template
import connexion
from flask_sqlalchemy import SQLAlchemy

connexion_app = connexion.App(__name__, specification_dir='./')
connexion_app.add_api('swagger.yml')

app = connexion_app.app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dao/main_sqlite.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    connexion_app.run(port=8001, debug=True)
