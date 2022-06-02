from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
    jsonify
)
from database.models import User, TodoList, db
from flask_login import current_user, login_required
from utils import (
    length_validator,
    email_validator,
    Pagination,
    data_rules
)
from sqlalchemy.exc import SQLAlchemyError
import math

user = Blueprint("user", __name__, template_folder="templates")


@user.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    user = User.query.get(current_user.get_id())
    if request.method == "POST":
        json_data = request.get_json()
        response = {
            "messages": [],
            "code": 200,
            "success": True
        }
        username = json_data["username"] or None
        email = json_data["email"] or None
        if username:
            if username != user.username:
                if not User.query.filter_by(username=username).first():
                    if length_validator(username):
                        user.username = username
                        response["messages"].append(
                            "Username successfully updated!")
                    else:
                        response["messages"].append("Username is weak")
                        response["code"] = 400
                        response["success"] = False
                else:
                    response["messages"].append(
                        "User with given username is exists!")
                    response["code"] = 400
                    response["success"] = False
            else:
                response["messages"].append(
                    "You've given me same username to update :D, so i didn't update it! OK?")
        if email:
            if email != user.email:
                if not User.query.filter_by(email=email).first():
                    if email_validator(email):
                        user.email = email
                        response["messages"].append(
                            "Email successfully updated!")
                    else:
                        response["messages"].append("Email is wrong")
                        response["code"] = 400
                        response["success"] = False
                else:
                    response["messages"].append(
                        "User with given email is exists!")
                    response["code"] = 400
                    response["success"] = False
            else:
                response["messages"].append(
                    "You've given me same email to update :D, so i didn't update it! OK?")
        try:
            user.update()
        except SQLAlchemyError:
            response["messages"].append("Something went wrong!")
            response["code"] = 422
            response["success"] = False
        finally:
            db.session.close()
        return jsonify(response), response["code"]

    paginate = Pagination()
    todo_lists = TodoList.query.filter_by(owner=user).order_by(TodoList.id).all()
    todo_lists = paginate.paginate_item(request, todo_lists)

    return render_template("user/profile.html",
                           user=user, todo_lists=todo_lists,
                           pages=math.ceil(len(user.todo_lists) / 5),
                           data_rules=data_rules)
