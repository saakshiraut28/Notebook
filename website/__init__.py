from flask import Flask

# Initialize our application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'some string'

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/') # '/' means no prefix 
    app.register_blueprint(auth, url_prefix='/')
    return app