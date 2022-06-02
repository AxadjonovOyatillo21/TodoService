from flask import (
    Flask,
    Blueprint,
    render_template,
    url_for
)
from auth import auth
from user import user
from main import main
from main_manager import main_manager
from api import api
from database.models import db, setup_db, User
from flask_login import LoginManager


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object("config.Config")
    db = setup_db(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.register_blueprint(main)
    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(main_manager)
    app.register_blueprint(api)

    return app
