from flask_sqlalchemy import SQLAlchemy

# Database configuration
#first need to install library
#pip install flask_sqlalchemy
#and create a database in the same folder as the app.py file
#sqlite:///database.db
#This is the path to the database file

db = SQLAlchemy()#This is the object that will allow us to interact with the database