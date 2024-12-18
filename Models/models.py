from Database.config import db


class User(db.Model):
    __tablename__ = 'users'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # Clave primaria
    name = db.Column(db.String(100), nullable=False)  # Nombre del usuario
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email único




class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    #relacion se define asi
    products = db.relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)


    #vamos a hacer la relacion entre pdocutos y categoria

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
