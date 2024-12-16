from Database.config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria
    name = db.Column(db.String(100), nullable=False)  # Nombre del usuario
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email único
