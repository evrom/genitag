from bottle import request
from passlib.hash import pbkdf2_sha256
from passlib.utils import to_bytes
from libraries.template import render_template
from sqlalchemy import exc
from libraries.database import engine as db
from libraries.forms import NewUser as Form
from libraries.status import Status
from libraries.insert import newuser as newuser_query
from libraries.messages import email_verify


def newuser():
    status = Status()
    form = Form(request.forms,
                captcha={'ip_address': request['REMOTE_ADDR']})
    if request.method == 'POST':
        if form.validate():
            new_pbkdf2 = to_bytes(pbkdf2_sha256.encrypt(form.password.data))
            username_lower = str.lower(form.username.data)
            try:
                conn = db.engine.connect()
                conn.execute(newuser_query,
                             username=username_lower,
                             email=form.email.data,
                             pbkdf2=new_pbkdf2)
                conn.close()
            except exc.SQLAlchemyError as message:
                status.danger = message
            else:
                email_verify(username_lower, form.email.data)
                return render_template(
                    'newuser_made.html',
                    status=status,
                    username=username_lower,
                    email=form.email.data)
        else:
            if 'captcha' in form.errors:
                status.warning = form.errors['captcha']
    return render_template('newuser.html', status=status, form=form)
