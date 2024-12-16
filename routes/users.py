from flask import Blueprint, request
from Models.models import User
from Database.config import db
#TODO 
"""
estdudiar bien esto mañana para entender todo el funcionamiento

"""
user = Blueprint('user', __name__)

@user.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return {"message": "Usuario registrado exitosamente!"}, 201


@user.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return {"users": [{"id": u.id, "name": u.name, "email": u.email} for u in users]}
