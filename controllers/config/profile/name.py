from bottle import Bottle, request
from sqlalchemy import exc
from libraries.database import engine as db
from libraries.template import view
from libraries.status import Status
from libraries.authentication import login_required
from libraries.forms import Name as Form
from libraries.forms import Blank as BlankForm
from libraries.insert import name as name_insert
from libraries.select import name as name_select
from libraries.delete import name as name_delete
from libraries.session import open_session
app = Bottle()


@app.route('/config/profile/name', method=['POST', 'GET'])
@view('config/profile/name.html')
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
                conn.execute(name_insert,
                             name=form.name.data,
                             username=username)
                conn.close()
                status.success = "Updated name"
            except exc.SQLAlchemyError as message:
                status.danger = message
    if request.method == 'POST' and\
       request.query['action'] == 'delete':
        blank_form = BlankForm(request.forms)
        if blank_form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(name_delete,
                             username=username)
                conn.close()
                status.success = "Deleted name"
            except exc.SQLAlchemyError as message:
                status.danger = message
    conn = db.engine.connect()
    result = conn.execute(name_select,
                          username=username)
    conn.close()
    row = result.fetchone()
    form.name.data = row['name']
    return dict(status=status, form=form)
