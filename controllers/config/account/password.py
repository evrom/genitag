from bottle import Bottle, request
from sqlalchemy.sql import select
from passlib.hash import pbkdf2_sha256
from passlib.utils import to_bytes
from libraries.template import view
from libraries.authentication import login_required
from libraries.status import Status
from libraries.database import users, engine as db
from libraries.session import open_session
from libraries.config.account.forms import Password as Form
app = Bottle()


@app.route('/config/account/password', method=['GET', 'POST'])
@view('/config/account/password.html')
@login_required
def index_page():
    status = Status()
    form = Form(request.forms)
    username = open_session()['u']
    if request.method == 'POST' and form.validate():
        conn = db.engine.connect()
        result = conn.execute(
            select([
                users.c.pbkdf2]).where(
                    users.c.id == username))
        conn.close()
        row = result.fetchone()
        verify = pbkdf2_sha256.verify(
            form.current_password.data, row['pbkdf2'])
        if verify:
            new_pbkdf2 = to_bytes(pbkdf2_sha256.encrypt(
                form.new_password.data))
            conn = db.engine.connect()
            conn.execute(
                users.update().values(
                    pbkdf2=new_pbkdf2).where(
                        users.c.id == username))
            conn.close()
            status.success = "Changed password"
        else:
            status.warning = "Wrong password for this account"
    return dict(status=status,
                form=form)
