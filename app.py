from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setting up Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# For the users
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(10),nullable=False)
    permission = db.Column(db.Integer, nullable=False)
    def __ref___(self): # for representation
        return f"{self.name} and {self.email}"

# Records
class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    date = db.Column(db.DateTime(),nullable=False)
    meal = db.Column(db.String(200),nullable=False)
    calories = db.Column(db.Integer,nullable=True)

# Permissions
class Permissions(db.Model):
    p_id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(200),nullable=False)

# Index Page
@app.route('/')
def index():
    return("Hello")

# List all the permissions
@app.route('/Permissions')
def list_permission():
    user_permission = Permissions.query.all()
    output = []
    for permission in user_permission:
        data = {'id' : permission.p_id, "name": permission.p_name}
        output.append(data)
    return{'permisions': output}

# List all the users [admin and user_manager]
@app.route('/Users')
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {'name': user.name, 'email': user.email}
        output.append(user_data)
    return{"user": output}

