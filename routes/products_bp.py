"""
2⃣ Ruta en Flask
Crea un Blueprint llamado products_bp que tenga dos rutas:

GET /products:

Devuelve la lista de productos renderizada en una página HTML.
POST /products:

Recibe datos enviados desde un formulario HTML.
Añade un nuevo producto utilizando el método add_product() de la clase de servicio.
Redirige a la ruta GET /products para mostrar la lista actualizada.

"""


from flask import Blueprint, request, jsonify
from Database.config import db


products_bp = Blueprint('products_bp', __name__)


@products_bp.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return jsonify({'message': 'GET method'}), 200
    elif request.method == 'POST':
        return jsonify({'message': 'POST method'}), 200
    else:
        return jsonify({'message': 'Method not allowed'}), 405

