from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	role = db.Column(db.Integer, unique = False)
	username = db.Column(db.Text, unique=True)
	password = db.Column(db.Text, unique=False)
	university_id = db.Column(db.Integer,unique = False)


class University(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Text, unique = True)

class Roles(db.Model):
    role = db.Column(db.Integer, primary_key = True)
    role_name = db.Column(db.Text,unique = True)
    admin_panel = db.Column(db.Boolean,unique = False)
    form_access = db.Column(db.Boolean,unique = False)

class Form(db.Model):
    role = db.Column(db.Integer, primary_key = True)
    info = db.Column(db.JSON)
    university_id = db.Column(db.Integer, unique = False)
