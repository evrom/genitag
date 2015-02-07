from bottle import request
from sqlalchemy import exc
from libraries.database import engine as db
from libraries.template import view
from libraries.status import Status
from libraries.authentication import login_required
from libraries.forms import ContactEmail as Form
from libraries.forms import Blank as BlankForm
from libraries.insert import contactemail as contactemail_insert
from libraries.select import contactemail as contactemail_select
from libraries.delete import contactemail as contactemail_delete
from libraries.session import open_session


@view('config/profile/contactemail.html')
@login_required
def contactemail():
    status = Status()
    form = Form(request.forms)
    username = open_session()['u']
    if request.method == 'POST' and\
       request.query['action'] == 'update':
        if form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(contactemail_insert,
                             contactemail=form.contactemail.data,
                             pgpmirror=form.pgpmirror.data,
                             pgpfingerprint=form.pgpfingerprint.data,
                             username=username)
                conn.close()
                status.success = "Updated Contact Email"
            except exc.SQLAlchemyError as message:
                status.danger = message
    if request.method == 'POST' and\
       request.query['action'] == 'delete':
        blank_form = BlankForm(request.forms)
        if blank_form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(contactemail_delete,
                             username=username)
                conn.close()
                status.success = "Deleted Contact Email"
            except exc.SQLAlchemyError as message:
                status.danger = message
    conn = db.engine.connect()
    result = conn.execute(contactemail_select,
                          username=username)
    conn.close()
    row = result.fetchone()
    form.contactemail.data = row['contactemail']
    form.pgpmirror.data = row['pgpmirror']
    form.pgpfingerprint.data = row['pgpfingerprint']
    return dict(status=status, form=form)
