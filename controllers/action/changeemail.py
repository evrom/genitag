from bottle import request, abort
from itsdangerous import URLSafeSerializer
from libraries.database import engine as db, users
from sqlalchemy.sql import select
from passlib.hash import pbkdf2_sha256
from libraries.template import render_template
from libraries.status import Status
from libraries.forms import ChangeEmail as Form
from sqlalchemy import exc
from libraries.csrf import csrf
from configuration import config
secret_key = config['app']['SECRET_KEY']
salt = config['app']['CHANGE_EMAIL_SALT']


@csrf
def changeemail():
    status = Status()
    form = Form(request.forms)
    s = URLSafeSerializer(secret_key, salt=salt)
    token = request.query.token
    try:
        deserialized_token = s.loads(request.query.token)
    except:
        return abort(500, 'bad signature')
    else:
        new_email = deserialized_token['e']
        username = deserialized_token['u']
        if request.method == 'POST' and form.validate():
            try:
                conn = db.engine.connect()
                result = conn.execute(
                    select([
                        users.c.pbkdf2]).where(
                            users.c.id == username))
                conn.close()
                row = result.fetchone()
                verify = pbkdf2_sha256.verify(
                    form.password.data, row['pbkdf2'])
                if verify:
                    conn = db.engine.connect()
                    conn.execute(users.update().values(
                        email=new_email).where(users.c.id == username))
                    conn.close()
                    status.success = "Email changed"
                    return render_template('/status.html',
                                           status=status)
                else:
                    status.warning = "Wrong password for this account"
            except exc.SQLAlchemyError as message:
                status.danger = message
    return render_template('/action/changeemail.html',
                           status=status,
                           form=form,
                           username=username,
                           new_email=new_email,
                           token=token)
