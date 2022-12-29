from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    jsonify
)
from src.database.models import (
    User,
    TodoList
)
from sqlalchemy.exc import SQLAlchemyError
from flask_login import (
    current_user,
    login_required
)
from src.user.update_operations import (
    update_profile
)
from src.validators_tools.common_validators import (
    length_validator,
    data_rules
)
from src.validators_tools.auth_validators import email_validator
from src.validators_tools.todo_list_todo_validators import Pagination
from math import ceil as math_ceil

user = Blueprint("user", __name__, template_folder="templates")


@user.route("/profile", methods=["GET", "PATCH"])
@login_required
def profile():
    user = User.query.get(current_user.get_id())
    if request.method == "PATCH":
        json_data = request.get_json()
        response = update_profile(user, json_data)
        return jsonify(response), response["code"]

    paginate = Pagination()
    todo_lists = TodoList.query.filter_by(
        owner=user).order_by(TodoList.id).all()
    todo_lists = paginate.paginate_item(request, todo_lists)

    return render_template("user/profile.html",
                           user=user, todo_lists=todo_lists,
                           pages=math_ceil(len(user.todo_lists) / 5),
                           data_rules=data_rules)
