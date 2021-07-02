from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    # Initialize app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '$rbn'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Register external routes as blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Initialize Database
    from .models import User, Post
    create_database(app)

    return app

# Creates database.db file in path if doesn't exist
def create_database(app):
    if not path.exists('database/' + DB_NAME):
        db.create_all(app=app)
        print('Database Doesn\'t exist. New database created!')