import functools

from flask import g
from flask import redirect, url_for


def sign_in_required(view):
    @functools.wraps(view)
    def wrapper(**kwargs):
        if g.user is None:
            return redirect(url_for('user_service.sign_in'))
        return view(**kwargs)

    return wrapper
