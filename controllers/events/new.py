from bottle import Bottle, request, redirect
from datetime import datetime
from libraries.template import view
from libraries.status import Status
from libraries.forms import NewEvent as Form
from libraries.authentication import login_required
from libraries.database import engine as db
from libraries.session import open_session
from sqlalchemy import exc
from libraries.insert import event as insert
app = Bottle()


@app.route('/events/new', method=['GET', 'POST'])
@view('/events/new.html')
@login_required
def index_page():
    status = Status()
    form = Form(request.forms)
    username = open_session()['u']
    if request.method == 'POST' and form.validate():
        try:
            event_datetime = datetime.strptime(
                form.date.data + ' ' + form.time.data,
                '%Y/%m/%d %I:%M %p')
        except:
            status.danger = "Date or time not in valid format. " + \
                            "Use selector buttons to select date and time"
        else:
            try:
                conn = db.engine.connect()
                result = conn.execute(insert,
                                      user_id=username,
                                      title=form.title.data,
                                      description=form.description.data,
                                      location=form.location.data,
                                      event_datetime=event_datetime)
                conn.close()
            except exc.SQLAlchemyError as message:
                status.danger = message
            else:
                redirect("/events/" + str(result.lastrowid))
    return dict(status=status,
                form=form)
