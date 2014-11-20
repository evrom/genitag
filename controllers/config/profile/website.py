from bottle import Bottle, request
from sqlalchemy import exc
from libraries.database import engine as db
from libraries.template import view
from libraries.status import Status
from libraries.authentication import login_required
from libraries.forms import Blank as BlankForm
from libraries.config.profile.forms import Website as Form
from libraries.config.profile.insert import website as insert
from libraries.config.profile.select import website as select
from libraries.config.profile.delete import website as delete
from libraries.session import open_session
app = Bottle()


@app.route('/config/profile/website', method=['POST', 'GET'])
@view('config/profile/website.html')
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
                conn.execute(insert,
                             websiteurl=form.websiteurl.data,
                             username=username)
                conn.close()
                status.success = "Updated Website URL"
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
                status.success = "Deleted Website URL"
            except exc.SQLAlchemyError as message:
                status.danger = message
    conn = db.engine.connect()
    result = conn.execute(select,
                          username=username)
    conn.close()
    row = result.fetchone()
    form.websiteurl.data = row['websiteurl']
    return dict(status=status, form=form)
