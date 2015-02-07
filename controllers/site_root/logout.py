from bottle import redirect
from libraries.session import remove_session


def logout():
    remove_session()
    return redirect('/')
