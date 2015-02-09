from bottle import request, abort
from itsdangerous import URLSafeSerializer
from libraries.database import engine as db, users
from libraries.template import view
from libraries.status import Status
from sqlalchemy import and_
from sqlalchemy import exc
from configuration import config
secret_key = config['app']['SECRET_KEY']
salt = config['app']['EMAIL_VERIFY_SALT']


@view('status.html')
def accountverify():
    status = Status()
    s = URLSafeSerializer(secret_key, salt=salt)
    try:
        token = s.loads(request.query.token)
    except:
        return abort(500, 'bad signature')
    else:
        try:
            conn = db.engine.connect()
            conn.execute(users.update().where(and_(
                users.c.id == token['u'], users.c.email == token['e'])).values(
                    emailverified=True))
        except exc.SQLAlchemyError as message:
            status.danger = message
        else:
            status.success = 'Email Verified'
    return dict(status=status)
