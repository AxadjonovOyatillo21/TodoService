from flask_login import login_user, logout_user, current_user
from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash
)
from database.models import User, db
from sqlalchemy.exc import SQLAlchemyError
from utils import (
    is_true,
    length_validator,
    password_validator,
    email_validator
)


auth = Blueprint("auth", __name__, url_prefix="/auth",
                 template_folder="templates")


@auth.route("/register", methods=["POST", "GET"])
def register():
    if not current_user.is_anonymous and current_user.is_authenticated:
        return redirect(url_for("user.profile"))
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        try:
            if length_validator(username) and password_validator(password)\
                    and email_validator(email):
                user_check_1 = User.query.filter_by(username=username).first()
                user_check_2 = User.query.filter_by(email=email).first()
                if is_true(user_check_1):
                    flash("This username already taken!")
                if is_true(user_check_2):
                    flash("User with this email is exists, try again!")
                if not is_true(user_check_1) and not is_true(user_check_2):
                    user = User(username=username,
                                email=email, password=password)
                    user.insert()
                    flash("Successfully registered!")
                    return redirect(url_for("auth.login"))
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
            flash("Error occured")
        finally:
            db.session.close()

    return render_template("auth/register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if not current_user.is_anonymous and current_user.is_authenticated:
        return redirect(url_for("user.profile"))
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        remember_me = request.form["remember"] or True
        if not username:
            flash("Please enter correct data(username)")
        if not password:
            flash("Please enter correct data(password)")
        if username and password:
            try:
                user = User.query.filter_by(username=username).first()
                if user:
                    if user.check_ph(password):
                        print(True)
                        login_user(user, remember=remember_me)
                        flash("Logged in successfully!")
                        return redirect(url_for("user.profile"))
                    else:
                        flash("Password is incorrect! Try again!")
                else:
                    flash("User with given username doesn't exists!")
            except SQLAlchemyError:
                flash("An error occured, try again please :/")
    return render_template("auth/sign_in.html")


@auth.route('/logout')
def logout():
    logout_user()
    flash("Logged out successfully!")
    return redirect(url_for("auth.login"))
