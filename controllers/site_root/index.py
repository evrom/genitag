import random
from libraries.template import view
from libraries.database import engine as db
from libraries.select import upcoming_events as upcoming_select
from datetime import datetime, timedelta

@view('index.html')
def index():
    conn = db.engine.connect()
    result = conn.execute(upcoming_select,
                          datetime_cutoff=(datetime.utcnow()
                                           - timedelta(seconds=11*3600)),
                          limit=3,
                          offset=0)
    conn.close()
    photo_number = random.randint(1, 11)
    return dict(photo_number=photo_number, result=result)
