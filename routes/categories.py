from flask import Blueprint
from flask import request

categories  = Blueprint('categories', __name__)



@categories.route('/categorias', methods=['GET', 'POST'])
def categorias():
    if request.method == 'POST':
        return {"mensaje": "Categoría creada"}
    else:
        return {"categorias": ["Programación", "Diseño", "Marketing"]}


