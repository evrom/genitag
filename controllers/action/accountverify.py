from bottle import Bottle, request
from libraries.signer import unsign_message
from libraries.database import engine as db, users
from libraries.template import view
from libraries.status import Status
from sqlalchemy import and_
from sqlalchemy import exc
app = Bottle()


@app.route('/action/accountverify', method=['GET'])
@view('action/emailverify.html')
def newuser():
    status = Status()
    token = unsign_message(request.query.token)
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