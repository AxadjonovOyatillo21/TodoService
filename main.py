from flask import (
    Blueprint,
    url_for,
    redirect,
    render_template
)
from flask_login import current_user


main = Blueprint("main", __name__)


@main.route('/')
def index():
    if not current_user.is_anonymous:
        if current_user.is_authenticated:
            return redirect(url_for("user.profile"))
    return render_template("index.html")