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


from flask import Blueprint, request, redirect, url_for, render_template
#from Database.config import db
from Services.productService import ProductService

products_bp = Blueprint('products_bp', __name__)
Products = ProductService()


@products_bp.route('/products', methods=['GET', 'POST'])
def manage_products():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        Products.add_product(name, price, category)
        # Redirige de vuelta a /products
        return redirect(url_for('products_bp.manage_products'))


    Products.get_products()
    return render_template('products.html', products=Products.get_products())
