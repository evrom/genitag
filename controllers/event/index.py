from bottle import Bottle
from libraries.template import view
from libraries.status import Status
import datetime
app = Bottle()


@app.route('/event', method='GET')
@view('/event/index.html')
def index_page():
    status = Status()
    description = "HI http://google.com/"
    return dict(status=status,
                description=description,
                datetime=datetime.datetime.utcnow())
