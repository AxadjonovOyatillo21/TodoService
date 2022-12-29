from flask import Blueprint, jsonify
from src.database.models import User


api_auth = Blueprint("api_auth", __name__, url_prefix="/auth")

@api_auth.route("/sign-up")
def sign_up():
    return {
        "message": "sign up route"
    }

@api_auth.route("/users")
def list_users():
    return jsonify(User.query.all()[-1].format())