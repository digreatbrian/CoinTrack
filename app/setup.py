from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app(name=__name__):
    from config import Config

    app = Flask(name)

    # Configuration
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

    # Initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Import Blueprints
    from .routes import main as main_blueprint

    # Register Blueprints
    app.register_blueprint(main_blueprint)

    # Additional setup
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User  # Import inside to avoid circular imports
        return User.query.get(int(user_id))

    # Set login view
    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    return app
