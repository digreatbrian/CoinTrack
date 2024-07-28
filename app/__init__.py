from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Import Blueprints
    from .main.routes import main as main_blueprint
    from .auth.routes import auth as auth_blueprint
    from .income.routes import income as income_blueprint
    from .expenses.routes import expenses as expenses_blueprint

    # Register Blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(income_blueprint)
    app.register_blueprint(expenses_blueprint)

    # Import models
    from app import models

    # Additional setup
    @login_manager.user_loader
    def load_user(user_id):
        from .models import User  # Import inside to avoid circular imports
        return User.query.get(int(user_id))

    # Set login view
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    return app
