from bottle import Bottle, request
from sqlalchemy import exc
from libraries.database import engine as db
from libraries.template import view
from libraries.status import Status
from libraries.authentication import login_required
from libraries.config.profile.forms import Github as Form
from libraries.forms import Blank as BlankForm
from libraries.config.profile.insert import github as github_insert
from libraries.config.profile.select import github as github_select
from libraries.config.profile.delete import github as github_delete
from libraries.session import open_session
app = Bottle()


@app.route('/config/profile/github', method=['POST', 'GET'])
@view('config/profile/github.html')
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
                conn.execute(github_insert,
                             githubname=form.githubname.data,
                             username=username)
                conn.close()
                status.success = "Updated Github Username"
            except exc.SQLAlchemyError as message:
                status.danger = message
    if request.method == 'POST' and\
       request.query['action'] == 'delete':
        blank_form = BlankForm(request.forms)
        if blank_form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(github_delete,
                             username=username)
                conn.close()
                status.success = "Deleted Github Username"
            except exc.SQLAlchemyError as message:
                status.danger = message
    conn = db.engine.connect()
    result = conn.execute(github_select,
                          username=username)
    conn.close()
    row = result.fetchone()
    form.githubname.data = row['githubname']
    return dict(status=status, form=form)
