from libraries.template import view
from libraries.status import Status
from libraries.select import event as select
from libraries.database import engine as db


@view('/events/event_page.html')
def event_page(id):
    status = Status()
    conn = db.engine.connect()
    result = conn.execute(select,
                          id=id)
    conn.close()
    row = result.fetchone()
    return dict(status=status, event_data=row)
