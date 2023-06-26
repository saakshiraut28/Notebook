from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize DB
db = SQLAlchemy()
DB_NAME = 'flask-data'

# Initialize our application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'some string'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #tells us where to create database
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') # '/' means no prefix 
    app.register_blueprint(auth, url_prefix='/') 

    from .models import User,Note

    create_database(app)

    # Where the user should be redirected if not logged in
    loginManager = LoginManager()
    loginManager.login_view='views.home'
    loginManager.init_app(app)

    @loginManager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Create a DB
def create_database(app):
    if not path.exists('website/'+DB_NAME):
         with app.app_context():
            db.create_all()
            print("Database Created")