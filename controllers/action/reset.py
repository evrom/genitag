from bottle import request, abort
from itsdangerous import URLSafeTimedSerializer
from libraries.database import engine as db, users
from passlib.hash import pbkdf2_sha256
from passlib.utils import to_bytes
from libraries.template import render_template
from libraries.status import Status
from libraries.forms import ResetPassword as Form
from sqlalchemy import exc
from libraries.csrf import csrf
from configuration import config
secret_key = config['app']['SECRET_KEY']
salt = config['app']['RESET_PASSWORD_SALT']


@csrf
def reset():
    status = Status()
    form = Form(request.forms)
    token = request.query.token
    s = URLSafeTimedSerializer(secret_key, max_age=3600, salt=salt)
    try:
        username = s.loads(token)
    except:
        return abort(500, 'bad signature')
    else:
        if request.method == 'POST' and form.validate():
            new_pbkdf2 = to_bytes(pbkdf2_sha256.encrypt(form.password.data))
            try:
                conn = db.engine.connect()
                conn.execute(users.update().values(
                    pbkdf2=new_pbkdf2).where(users.c.id == username))
                conn.close()
            except exc.SQLAlchemyError as message:
                status.danger = message
            else:
                status.success = 'Password Changed. Please log in.'
                return render_template('/status.html',
                                       status=status)
    return render_template('/action/reset.html',
                           status=status,
                           form=form,
                           username=username,
                           token=token)
