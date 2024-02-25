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
    username = json_data.get("username", None)
    email = json_data.get("email", None)

    if (username == user.username) and (email == user.email):
        response["messages"].append("Nothing to update")

    if username != user.username:

        if User.query.filter_by(username=username).first():

            response["messages"].append("User with this username exists")

        else:
            if not length_validator(username):

                response["messages"].append("Username is weak")

            else:

                user.username = username
                response["code"] = 200
                response["success"] = True
                response["messages"].append(
                    "Username was successfully updated")

    if email != user.email:

        if User.query.filter_by(email=email).first():

            if response["success"]:
                response["code"] = 400
                response["success"] = False
                response["messages"] = []

            response["messages"].append("User with this email exists")

        else:

            if not email_validator(email):

                if response["success"]:
                    response["code"] = 400
                    response["success"] = False
                    response["messages"] = []

                response["messages"].append("Bad email")

            else:

                user.email = email
                response["code"] = 200
                response["success"] = True
                response["messages"].append("Email was succesfully updated")

    if response["success"]:

        try:
            user.update()

        except SQLAlchemyError:

            response["code"] = 422
            response["success"] = False
            response["messages"] = ["Something went wrong"]

        finally:
            db.session.close()

    else:

        response["username"] = user.username
        response["email"] = user.email

    return response
