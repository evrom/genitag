from bottle import Bottle, request, redirect
from passlib.hash import pbkdf2_sha256
from libraries.template import view
from sqlalchemy import exc
from sqlalchemy.sql import select
from libraries.regex import email as EmailRegex,\
    username as UsernameRegex
from libraries.database import users, engine as db
from libraries.forms import Login as Form
from libraries.status import Status
from libraries.session import set_session
app = Bottle()


@app.route('/login', method=['GET', 'POST'])
@view('login.html')
def login():
    status = Status()
    form = Form(request.forms)
    if request.method == 'POST' and form.validate():
        if UsernameRegex.match(
                form.loginname.data) or EmailRegex.match(form.loginname.data):
            conn = db.engine.connect()
            try:
                if EmailRegex.match(form.loginname.data):
                    result = conn.execute(
                        select([
                            users.c.id,
                            users.c.pbkdf2,
                            users.c.emailverified]).where(
                                users.c.email == form.loginname.data))
                elif UsernameRegex.match(form.loginname.data):
                    result = conn.execute(
                        select([
                            users.c.id,
                            users.c.pbkdf2,
                            users.c.emailverified]).where(
                                users.c.id == form.loginname.data))
                row = result.fetchone()
                if row is not None:
                    verify = pbkdf2_sha256.verify(
                        form.password.data, row['pbkdf2'])
                    if verify:
                        if row['emailverified']:
                            set_session({'u': row['id']})
                            return redirect('/config')
                        else:
                            status.warning = "Email not verified"
                    else:
                        status.warning = "Wrong Password for Username/Email"
                else:
                        status.warning = "Username/Email not in Database"
            except exc.SQLAlchemyError as message:
                status.danger = message
            conn.close()
        else:
            status.warning = 'Not valid username or email'
    return dict(form=form, status=status)
