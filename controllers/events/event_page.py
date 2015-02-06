from bottle import Bottle
from libraries.template import view
from libraries.status import Status
from libraries.events.select import event as select
from libraries.database import engine as db
app = Bottle()


@app.route('/events/<id:int>/<:re>', method=['GET', 'POST'])
@app.route('/events/<id:int>', method=['GET', 'POST'])
@view('/events/event_page.html')
def index_page(id):
    status = Status()
    conn = db.engine.connect()
    result = conn.execute(select,
                          id=id)
    conn.close()
    row = result.fetchone()
    return dict(status=status, event_data=row)
