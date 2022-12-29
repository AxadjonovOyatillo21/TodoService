from flask import flash
from flask_login import (
    login_user
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from src.database.models import User, db
from src.validators_tools.auth_validators import (
    password_validator,
    email_validator
)
from src.validators_tools.common_validators import (
    length_validator
)


def sign_up(form):
    username = form.get("username") or None
    email = form.get("email") or None
    password = form.get("password") or None
    try:
        if length_validator(username)\
                and password_validator(password)\
                and email_validator(email):
            user_by_username = User.query.filter_by(
                username=username
            ).first()
            user_by_email = User.query.filter_by(
                email=email
            ).first()
            if user_by_username:
                flash("This username is already taken!")
            if user_by_email:
                flash("User with this email is already exists, try again!")
            if (not user_by_username) and (not user_by_email):
                user = User(username=username,
                            email=email, password=password)
                user.insert()
                flash("Successfully registered!")
                return True
        else:
            if not length_validator(username):
                flash("Bad username, try again!")
            if not email_validator(email):
                flash("Bad email, try again!")
            if not password_validator(password):
                flash(
                    "Password is bad or weak, enter characters more than 6, and try again!"
                )
    except SQLAlchemyError:
        flash("An error occured, try again please :/")
    finally:
        db.session.close()


def log_in(form):
    username = form.get("username") or \
        flash("Please enter correct data(username)")
    password = form.get("password") or \
        flash("Please enter correct data(password)")
    remember = form.get("remember") or False
    if username and password:
        try:
            user = User.query.filter_by(username=username).first()
            if user and user.check_ph(password):
                login_user(user, remember=remember)
                flash("Logged in successfully!")
                return True
            else:
                flash("Username or password is incorrect. Try again.")
        except SQLAlchemyError:
            flash("An error occured, try again please :/")
        finally:
            db.session.close()
