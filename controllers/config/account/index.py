from bottle import Bottle
from libraries.template import view
from libraries.authentication import login_required
from libraries.status import Status
app = Bottle()


@app.route('/config/account', method='GET')
@app.route('/config/account/', method='GET')
@view('/config/account/index.html')
@login_required
def index_page():
    status = Status()
    return dict(status=status)
