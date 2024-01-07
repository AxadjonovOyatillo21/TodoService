from flask import (
    Flask,
    Blueprint,
    render_template,
    url_for
)
from src.auth import auth
from src.user import user
from src.main import main
from src.main_manager import main_manager
from src.api import api
from src.database.models import db, setup_db, User
from flask_login import LoginManager


def create_app(test_config=None):
    app = Flask(__name__)

    with app.app_context():
        app.config.from_object("src.config")
        setup_db(app)
        login_manager = LoginManager()
        login_manager.init_app(app)
        login_manager.login_view = "auth.login"

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(user_id)

        blueprints = [main, user, auth, main_manager, api]
        for blueprint in blueprints:
            app.register_blueprint(blueprint)

        return app