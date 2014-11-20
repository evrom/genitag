from bottle import Bottle
from libraries.template import view
from libraries.authentication import login_required
from libraries.status import Status
app = Bottle()


@app.route('/config/', method='GET')
@app.route('/config', method='GET')
@view('/config/index.html')
@login_required
def index_page():
    status = Status()
    return dict(status=status)
