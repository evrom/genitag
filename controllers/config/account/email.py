from bottle import Bottle, request
from sqlalchemy.sql import select
from passlib.hash import pbkdf2_sha256
from libraries.template import view
from libraries.authentication import login_required
from libraries.status import Status
from libraries.database import users, engine as db
from libraries.session import open_session
from libraries.config.account.forms import Email as Form
from libraries.config.account.email import change_email
app = Bottle()


@app.route('/config/account/email', method=['GET', 'POST'])
@view('/config/account/email.html')
@login_required
def index_page():
    status = Status()
    form = Form(request.forms)
    username = open_session()['u']
    if request.method == 'POST' and form.validate():
        change_email(username, form.email.data)
        status.success = "Sending email to " + form.email.data
    conn = db.engine.connect()
    result = conn.execute(
        select([
            users.c.email]).where(
                users.c.id == username))
    conn.close()
    row = result.fetchone()
    email = row['email']
    return dict(status=status,
                form=form,
                email=email)
