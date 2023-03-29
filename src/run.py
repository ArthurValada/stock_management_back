from flask import render_template
import connexion
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(port=8001, debug=True)
    from model.employee import Employee
    STORAGE = {
        42: Employee(42, 'nome', 'data', 'm', '2020202', 'senha', 2, True)  # todo: serializar isto
    }  # Variável apenas para uso em testes. todo: remover isto
