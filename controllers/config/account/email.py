from bottle import Bottle, request
from sqlalchemy.sql import select
from libraries.template import view
from libraries.authentication import login_required
from libraries.status import Status
from libraries.database import users, engine as db
from libraries.session import open_session
from libraries.forms import SendEmail as Form
from libraries.messages import change_email
app = Bottle()


@app.route('/config/account/email', method=['GET', 'POST'])
@view('/config/account/email.html')
@login_required
def index_page():
    status = Status()
    form = Form(request.forms,
                captcha={'ip_address': request['REMOTE_ADDR']})
    username = open_session()['u']
    if request.method == 'POST' and form.validate():
        change_email(username, form.email.data)
        status.success = "Sending email to " + form.email.data
    else:
        if 'captcha' in form.errors:
            status.warning = form.errors['captcha']
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
