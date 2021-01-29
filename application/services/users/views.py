from flask import Blueprint
from flask import render_template, redirect, flash
from flask import request, session, url_for, g
from flask_login import current_user, login_user, logout_user

from application.services.users.models import User
from application.utils.login import login

user_bp = Blueprint('user_service', __name__, url_prefix='/user')


@user_bp.before_app_request
def load_signed_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


@user_bp.route('/signup', methods=('GET', 'POST'))
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        user = User.query.filter_by(username=username).first()
        if user is not None:
            error = f'User {username} is already exists'

        if error is None:
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save_to_db()
            return redirect(url_for('user_service.sign_in'))
        
        flash(error)

    return render_template("auth/sign_up.html")


@user_bp.route('/signin', methods=('GET', 'POST'))
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        user = User.query.filter_by(username=username).first()
        if user is None:
            error = 'Incorrect username!'
        elif not user.check_password(password):
            error = 'Incorrect password!'

        if error is None:
            login_user(user)
            return redirect(url_for('index'))

        flash(error)

    return render_template("auth/sign_in.html")


@user_bp.route('/signout')
def sign_out():
    logout_user()
    return redirect(url_for('index'))


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

