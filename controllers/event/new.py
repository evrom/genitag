from bottle import Bottle, request
from datetime import datetime
from libraries.template import view
from libraries.status import Status
from libraries.event.forms import NewEvent as Form
from libraries.authentication import login_required
from libraries.database import engine as db
from libraries.database import events
from libraries.session import open_session
from sqlalchemy import exc
app = Bottle()


@app.route('/event/new', method=['GET', 'POST'])
@view('/event/new.html')
@login_required
def index_page():
    status = Status()
    form = Form(request.forms)
    username = open_session()['u']
    if request.method == 'POST' and form.validate():
        print(form.location.data)
        print(form.title.data)
        try:
            event_datetime = datetime.strptime(
                form.date.data + ' ' + form.time.data,
                '%Y/%m/%d %I:%M %p')
            print(event_datetime)
        except:
            status.danger = "Date or time not in valid format. " + \
                            "Use selector buttons to select date and time"
        else:
            try:
                conn = db.engine.connect()
                conn.execute(events.insert().values(
                    user_id=username,
                    title=form.title.data,
                    info=form.description.data,
                    location=form.location.data,
                    event_datetime=event_datetime))
                conn.close()
                status.success = "Added Event"
            except exc.SQLAlchemyError as message:
                status.danger = message
    return dict(status=status,
                form=form)
