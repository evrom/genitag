from bottle import Bottle, request
from sqlalchemy import exc
from gravatar import Gravatar
from urllib.parse import urlparse
from libraries.database import engine as db
from libraries.template import view
from libraries.status import Status
from libraries.authentication import login_required
from libraries.config.profile.forms import Avatar as Form
from libraries.forms import Blank as BlankForm
from libraries.config.profile.select import avatar as avatar_select
from libraries.config.profile.insert import avatar as avatar_insert
from libraries.config.profile.delete import avatar as avatar_delete
from libraries.session import open_session
app = Bottle()


@app.route('/config/profile/avatar', method=['GET', 'POST'])
@view('config/profile/avatar.html')
@login_required
def profile():
    status = Status()
    form = Form(request.forms)
    username = open_session()['u']
    if request.method == 'POST' and\
       request.query['action'] == 'update':
        if form.validate():
            use_custom_avatar = False
            do_insert = False
            avatar_url = urlparse(form.avatar_url.data)
            if avatar_url.netloc == 'avatars.io' or\
               not bool(avatar_url.netloc):
                do_insert = True
            else:
                status.warning = "Invalid custom avatar"
            if form.avatar_type.data == 'avatarsio':
                if avatar_url.netloc == 'avatars.io':
                    use_custom_avatar = True
                else:
                    do_insert = False
            if do_insert:
                try:
                    conn = db.engine.connect()
                    conn.execute(avatar_insert,
                                 customavatarurl=avatar_url.geturl(),
                                 usecustomavatar=use_custom_avatar,
                                 username=username)
                    conn.close()
                    status.success = "Updated Avatar"
                except exc.SQLAlchemyError as message:
                    status.danger = message
    if request.method == 'POST' and\
       request.query['action'] == 'delete':
        blank_form = BlankForm(request.forms)
        if blank_form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(avatar_delete,
                             username=username)
                conn.close()
                status.success = "Deleted Twitter Handle"
            except exc.SQLAlchemyError as message:
                status.danger = message
    conn = db.engine.connect()
    result = conn.execute(avatar_select,
                          username=username)
    conn.close()
    row = result.fetchone()
    gravatar_url = Gravatar(row['email'], size=128).thumb
    return dict(status=status,
                form=form,
                gravatar_url=gravatar_url,
                custom_avatar_url=row['customavatarurl'],
                use_custom_avatar=bool(row['usecustomavatar']))
