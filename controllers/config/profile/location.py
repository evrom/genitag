from bottle import Bottle, request
from sqlalchemy import exc
from libraries.database import engine as db
from libraries.template import view
from libraries.status import Status
from libraries.authentication import login_required
from libraries.config.profile.forms import Location as Form
from libraries.forms import Blank as BlankForm
from libraries.config.profile.insert import location as location_insert
from libraries.config.profile.select import location as location_select
from libraries.config.profile.delete import location as location_delete
from libraries.session import open_session
app = Bottle()


@app.route('/config/profile/location', method=['POST', 'GET'])
@view('config/profile/location.html')
@login_required
def profile():
    status = Status()
    form = Form(request.forms)
    username = open_session()['u']
    if request.method == 'POST' and\
       request.query['action'] == 'update':
        if form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(location_insert,
                             location=form.location.data,
                             username=username)
                conn.close()
                status.success = "Updated Location"
            except exc.SQLAlchemyError as message:
                status.danger = message
    if request.method == 'POST' and\
       request.query['action'] == 'delete':
        blank_form = BlankForm(request.forms)
        if blank_form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(location_delete,
                             username=username)
                conn.close()
                status.success = "Deleted Location"
            except exc.SQLAlchemyError as message:
                status.danger = message
    conn = db.engine.connect()
    result = conn.execute(location_select,
                          username=username)
    conn.close()
    row = result.fetchone()
    form.location.data = row['location']
    return dict(status=status, form=form)
