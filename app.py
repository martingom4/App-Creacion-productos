from flask import Flask
from Database.config import db
from routes.products_bp import products_bp

app = Flask(__name__)
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MARgomlcmajm100@localhost/Prueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()
    print("Tablas creadas en PostgreSQL") # Crea las tablas definidas en models.py
app.register_blueprint(products_bp)

if __name__ == '__main__':
    app.run()