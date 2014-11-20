from bottle import Bottle
from libraries.template import view
from libraries.status import Status
from sqlalchemy.sql import select
from libraries.database import engine as db
from libraries.database import events
app = Bottle()


@app.route('/event/upcoming', method=['GET', 'POST'])
@view('/event/event_page.html')
def index_page():
    status = Status()
    conn = db.engine.connect()
    result = conn.execute(
        select([
            events.c.user_id,
            events.c.location,
            events.c.info,
            events.c.timestamp,
            events.c.title,
            events.c.event_datetime]))
    conn.close()
    return dict(status=status, event=result)
