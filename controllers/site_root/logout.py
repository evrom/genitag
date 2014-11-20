from bottle import Bottle, redirect
from libraries.session import remove_session
app = Bottle()


@app.route('/exit', method='GET')
def logout():
    remove_session()
    return redirect('/')
