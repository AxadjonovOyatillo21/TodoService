from flask import Blueprint 

api_auth = Blueprint("api_auth", __name__)

@api_auth.route("/auth/sign-up")
def sign_up():
    return {
        "message": "sign up route"
    }