from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    role = db.Column(db.Integer, unique = False)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text, unique=False)
    university_id = db.Column(db.Integer,unique = False)

    def __init__(self,username,password):
        hash = bcrypt.generate_password_hash(password).decode('utf-8')
        self.username = username
        self.password = hash

    def format(self):
        return {
            "id":self.id,
            "role":self.role,
            "username":self.username,
            "university_id":self.university_id
        }




class University(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, unique = True)

    def format(self):
        return {
            "id":self.id,
            "name":self.name
        }

class Roles(db.Model):
    role = db.Column(db.Integer, primary_key = True)
    role_name = db.Column(db.Text,unique = True)

    def format(self):
        return {
            "id":self.role,
            "name":self.role_name,
        }

class Form(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    info = db.Column(db.JSON)
    university_id = db.Column(db.Integer, unique = False)

    def format(self):
        return {
            "id":id,
            "data":info,
            "university_id":university_id
        }
