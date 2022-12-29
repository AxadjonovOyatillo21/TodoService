from flask import (
    Blueprint,
    jsonify,
    request
)
from src.database.models import (
    User, 
    TodoList, 
    Todo
)
from src.api.api_auth import api_auth 

api = Blueprint("api", __name__, url_prefix="/api")
api.register_blueprint(api_auth)

@api.route("/")
def hello():
    return jsonify({
        "message": "API works🎉"
    })

