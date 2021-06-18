from flask import Flask


def create_app():
    # Initialize app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '$rbn'

    # Register external routes as blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
