from bottle import Bottle, request, redirect
from passlib.hash import pbkdf2_sha256
from passlib.utils import to_bytes
from libraries.template import view
from sqlalchemy import exc
from libraries.database import engine as db
from libraries.site_root.forms import NewUser as Form
from libraries.status import Status
from libraries.site_root.insert import newuser as newuser_query
app = Bottle()


@app.route('/newuser', method=['POST', 'GET'])
@view('newuser.html')
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
                return redirect('/login')
        else:
            if 'captcha' in form.errors:
                status.warning = form.errors['captcha']
    return dict(status=status, form=form)
