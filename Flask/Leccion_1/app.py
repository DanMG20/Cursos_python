from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello_world():

    app.logger.info('Entramos al Path')
    return "<p>Hello, World! AKSADMALSM asdasdasdk</p>"


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre}'

