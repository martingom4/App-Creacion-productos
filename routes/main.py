from flask import Flask, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def hello_word():
    return 'Hello World!'

@main.route('/saludo/<name>')
def saludo(name):
    return {"mensaje": f"Hola {name}, bienvenido a mi API!"}

