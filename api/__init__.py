from flask import (
    Blueprint,
    jsonify,
    request
)
from database.models import (
    User, 
    TodoList, 
    Todo
)
from api.api_auth import api_auth 

api = Blueprint("api", __name__, subdomain="api")

@api.route("/")
def hello():
    return jsonify({
        "message": "API works🎉"
    })

api.register_blueprint(api_auth)