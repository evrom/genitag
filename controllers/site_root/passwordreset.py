from bottle import Bottle, request, redirect
from libraries.template import view
from sqlalchemy import exc
from sqlalchemy.sql import select
from libraries.regex import email as EmailRegex,\
    username as UsernameRegex
from libraries.database import users, engine as db
from libraries.site_root.forms import PasswordReset as Form
from libraries.status import Status
app = Bottle()


@app.route('/passwordrest', method=['GET', 'POST'])
@view('passwordreset.html')
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
                    pass
                else:
                        status.warning = "Username/Email not in Database"
            except exc.SQLAlchemyError as message:
                status.danger = message
            conn.close()
        else:
            status.warning = 'Not valid username or email'
    return dict(form=form, status=status)