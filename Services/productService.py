"""
Clase de Servicio
Crea una clase ProductsService con lo siguiente:

Un atributo self.products: una lista vacía al inicio.
Un método get_products(): Devuelve la lista de productos.
Un método add_product(name, price, category): Añade un nuevo producto a la lista. Cada producto debe ser un diccionario con las claves:
"name", "price", "category".

"""

class ProductService:
    def __init__(self):
        self.products = []

    def get_products(self):
        vacia = len(self.products)
        if vacia == 0:
            return "No hay productos"
        else:
            return self.products # devolvemos la lista de prodcutos que tenemos

    def add_product(self, name,price,category):
        self.products.append({"name": name, "price": price, "category": category})
        return self.products



