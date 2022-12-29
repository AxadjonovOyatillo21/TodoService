from src.database.models import (
    db,
    User
)
from sqlalchemy.exc import SQLAlchemyError
from src.validators_tools.common_validators import (
    length_validator
)
from src.validators_tools.auth_validators import (
    email_validator
)


def update_profile(user, json_data):
    response = {
        "messages": [],
        "code": 400,
        "success": False
    }
    messages = response["messages"]
    username = json_data.get("username") or None
    email = json_data.get("email") or None
    if username != user.username:
        if not User.query.filter_by(username=username).first():
            if length_validator(username):
                user.username = username
                messages.append(
                    "Username successfully updated!")
                response["code"] = 200
                response["success"] = True
            else:
                messages.append("Username is weak")
        else:
            messages.append(
                "User with given username is already exists!")
    else:
        messages.append(
            "You've given me same username to update :D, so i didn't update it! OK?")

    if email != user.email:
        if not User.query.filter_by(email=email).first():
            if email_validator(email):
                user.email = email
                messages.append(
                    "Email successfully updated!")
                response["code"] = 200
                if not response["success"]:
                    response["success"] = True
            else:
                messages.append("Email is wrong")
        else:
            messages.append(
                "User with given email is already exists!")
    else:
        messages.append(
            "You've given me same email to update :D, so i didn't update it! OK?")
    if response["code"] == 200:
        try:
            user.update()
        except SQLAlchemyError:
            messages.append("Something went wrong!")
            response["code"] = 422
            response["success"] = False
        finally:
            db.session.close()
    else:
        response["username"] = user.username
        response["email"] = user.email
    return response
