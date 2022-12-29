from flask_login import login_user, logout_user, current_user
from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash
)
from src.database.models import User, db
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from src.auth.auth_operations import (
    sign_up,
    log_in
)


auth = Blueprint("auth", __name__, url_prefix="/auth",
                 template_folder="templates")


@auth.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("user.profile"))
    if request.method == "POST":
        form = request.form
        if sign_up(form):
            return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("user.profile"))
    if request.method == "POST":
        form = request.form
        if log_in(form):
            return redirect(url_for("user.profile"))
    return render_template("auth/sign_in.html")


@auth.route('/logout')
def logout():
    logout_user()
    flash("Logged out successfully!")
    return redirect(url_for("auth.login"))
