from bottle import request
from libraries.database import engine as db, users
from libraries.template import view
from libraries.status import Status
from libraries.forms import SendEmail as Form
from sqlalchemy import exc
from sqlalchemy.sql import select
from libraries.messages import email_verify as send_email


@view('action/resend.html')
def resend():
    status = Status()
    form = Form(request.forms,
                captcha={'ip_address': request['REMOTE_ADDR']})
    if request.method == 'POST' and form.validate():
        try:
            conn = db.engine.connect()
            result = conn.execute(
                select([
                    users.c.id,
                    users.c.email,
                    users.c.emailverified]).where(
                        users.c.email == form.email.data))
            row = result.fetchone()
            if row is not None:
                if row['emailverified'] == True:
                    status.warning = "Email already verified"
                else:
                    send_email(row['id'], row['email'])
                    status.success = "Email Sent to " + row['email']
            else:
                status.warning = "Username/Email not in Database"
        except exc.SQLAlchemyError as message:
            status.danger = message
            conn.close()
    else:
        if 'captcha' in form.errors:
            status.warning = form.errors['captcha']
    return dict(status=status, form=form)
