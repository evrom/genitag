from bottle import request
from sqlalchemy import exc
from libraries.database import engine as db
from libraries.template import view
from libraries.status import Status
from libraries.authentication import login_required
from libraries.forms import Twitter as Form
from libraries.forms import Blank as BlankForm
from libraries.insert import twitter as insert
from libraries.select import twitter as select
from libraries.delete import twitter as delete
from libraries.session import open_session
from libraries.csrf import csrf


@view('config/profile/twitter.html')
@login_required
@csrf
def twitter():
    status = Status()
    form = Form(request.forms)
    username = open_session()['u']
    if request.method == 'POST' and\
       request.query['action'] == 'update':
        if form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(insert,
                             twittername=form.twittername.data,
                             username=username)
                conn.close()
                status.success = "Updated Twitter Handle"
            except exc.SQLAlchemyError as message:
                status.danger = message
    if request.method == 'POST' and\
       request.query['action'] == 'delete':
        blank_form = BlankForm(request.forms)
        if blank_form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(delete,
                             username=username)
                conn.close()
                status.success = "Deleted Twitter Handle"
            except exc.SQLAlchemyError as message:
                status.danger = message
    conn = db.engine.connect()
    result = conn.execute(select,
                          username=username)
    conn.close()
    row = result.fetchone()
    form.twittername.data = row['twittername']
    return dict(status=status, form=form)
