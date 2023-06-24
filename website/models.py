from . import db
from flask_login import UserMixin
from sqlalchemy import func

# Create a table for User Entity:
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150))
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))

# Create a table for Notes Entity:
class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    note = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())