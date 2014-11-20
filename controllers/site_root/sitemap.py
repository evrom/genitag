from bottle import Bottle
from libraries.template import view
# from libraries.status import Status
from sqlalchemy.sql import select
from libraries.database import engine as db
from libraries.database import events
app = Bottle()


@app.route('/sitemap.xml', method=['GET', 'POST'])
@view('/sitemap.xml')
def index_page():
    conn = db.engine.connect()
    event_result = conn.execute(
        select([
            events.c.id,
            events.c.timestamp,
            events.c.title]))
    conn.close()
    event_list = event_result.fetchall()
    for event in event_list:
        print(event['title'])
    return dict(event_list=event_list)
