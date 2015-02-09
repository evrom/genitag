from bottle import request
from libraries.template import view
from libraries.status import Status
from libraries.database import engine as db
from libraries.select import upcoming_events as upcoming_select,\
    previous_events as previous_select
from datetime import datetime, timedelta


@view('/events/list.html')
def upcoming():
    status = Status()
    try:
        offset = int(request.query['offset'])
    except:
        offset = 0
    if offset < 0:
        conn = db.engine.connect()
        raw_result = conn.execute(previous_select,
                                  datetime_cutoff=(datetime.utcnow()
                                                   - timedelta(
                                                       seconds=11*3600)),
                                  limit=15,
                                  offset=abs(offset + 15))
        result = raw_result.fetchall()[::-1]
    else:
        conn = db.engine.connect()
        result = conn.execute(upcoming_select,
                              datetime_cutoff=(datetime.utcnow()
                                               - timedelta(seconds=11*3600)),
                              limit=15,
                              offset=offset)
    conn.close()
    return dict(status=status, result=result, offset=offset)
