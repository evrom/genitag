from libraries.template import view
from libraries.status import Status
from sqlalchemy.sql import select
from libraries.database import engine as db
from libraries.database import events
from datetime import datetime, timedelta


@view('/events/list.html')
def upcoming():
    status = Status()
    conn = db.engine.connect()
    result = conn.execute(
        select([
            events.c.id,
            events.c.location,
            events.c.title,
            events.c.event_datetime]).where(
                events.c.event_datetime >
                (datetime.utcnow()
                 - timedelta(seconds=11*3600))).order_by(
                     events.c.event_datetime).limit(15))
    conn.close()
    return dict(status=status, result=result)
