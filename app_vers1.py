
from flask import Flask  # Importa o módulo Flask do pacote flask
# Instancia o objeto Flask passando o nome do script com seu path
from flask import render_template  # Função usada para redenrizar a página
# importa a classe Bootstrap em um arquivo Python
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# instancia um objeto Bootstrap
bootstrap = Bootstrap(app)


@app.route('/')  # Declara a rota padrão da aplicação
# registrando a função index()
# como tratador da URL raiz
def index():
    # return '<h1> ToDo </h1>'
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/listar/<int:n>')
def listar(n):
    return render_template('comments.html', lista=n)
