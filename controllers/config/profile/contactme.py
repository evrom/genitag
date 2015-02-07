from bottle import request
from sqlalchemy import exc
from libraries.database import engine as db
from libraries.template import view
from libraries.status import Status
from libraries.authentication import login_required
from libraries.forms import ContactMe as Form
from libraries.forms import Blank as BlankForm
from libraries.insert import contactme as description_insert
from libraries.select import contactme as description_select
from libraries.delete import contactme as description_delete
from libraries.session import open_session


@view('config/profile/description.html')
@login_required
def contactme():
    status = Status()
    form = Form(request.forms)
    username = open_session()['u']
    if request.method == 'POST' and\
       request.query['action'] == 'update':
        if form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(description_insert,
                             description=form.description.data,
                             username=username)
                conn.close()
                status.success = "Updated description"
            except exc.SQLAlchemyError as message:
                status.danger = message
    if request.method == 'POST' and\
       request.query['action'] == 'delete':
        blank_form = BlankForm(request.forms)
        if blank_form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(description_delete,
                             username=username)
                conn.close()
                status.success = "Deleted description"
            except exc.SQLAlchemyError as message:
                status.danger = message
    conn = db.engine.connect()
    result = conn.execute(description_select,
                          username=username)
    conn.close()
    row = result.fetchone()
    form.description.data = row['description']
    return dict(status=status, form=form, description_type="contactme")
