from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
db = SQLAlchemy()
mail = Mail()
photos = UploadSet('photos', IMAGES)
simple = SimpleMDE()
# Initializing app


def create_app(config_name):

    # Initializing app
    app = Flask(__name__)

    # Setting up Config
    app.config.from_object(config_options[config_name])

    # Initializing flask extension
    db.init_app(app)
    login_manager.init_app(app)

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # Registering the auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # configure UploadSet
    configure_uploads(app, photos)

    return app
