from flask import Flask
from routes.main import main
from routes.operations import operations
from Database.config import db
from routes.users import user


app = Flask(__name__)


# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MARgomlcmajm100@localhost/Prueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

with app.app_context():
    db.create_all()
    print("Tablas creadas en PostgreSQL") # Crea las tablas definidas en models.py

app.register_blueprint(main)
app.register_blueprint(operations)
app.register_blueprint(user)



if __name__ == '__main__':
    app.run()
