from flask import Blueprint
from flask import render_template

user_bp = Blueprint('user_service_bp', __name__, url_prefix='/user', template_folder='templates')


@user_bp.route('/register', methods=('GET', 'POST'))
def register():
    return render_template("auth/register.html")

