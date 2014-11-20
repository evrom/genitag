from functools import wraps
from bottle import abort
from .session import open_session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            open_session()
        except:
            abort(401)
        return f(*args, **kwargs)
    return decorated_function



