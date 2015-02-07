from bottle import request
from libraries.template import view
from libraries.status import Status
from libraries.djangoforms import Title as Form
from libraries.authentication import login_required
from libraries.select import event_by_user as select
from libraries.database import engine as db
from libraries.session import open_session
# from sqlalchemy import exc


# @app.route('/events/<id:int>/edit/', method=['GET', 'POST'])
@view('/events/edit.html')
@login_required
def edit(id):
    status = Status()
    username = open_session()['u']
    form = Form()
    conn = db.engine.connect()
    result = conn.execute(select,
                          id=id, username=username)
    conn.close()
    row = result.fetchone()
    return dict(status=status, event_id=row['id'], form=form)
