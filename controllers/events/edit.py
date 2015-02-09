from bottle import request
from libraries.template import view
from libraries.status import Status
from libraries.forms import EventTitle, EventDateTime,\
    EventLocation, EventDescription, EventFlags
from libraries.authentication import login_required
from libraries.select import event_by_user as select
from libraries.database import engine as db, events
from libraries.session import open_session
from libraries.update import description as description_update,\
    flags as flags_update
from sqlalchemy import exc, and_
from datetime import datetime
from libraries.csrf import csrf


@view('/events/edit.html')
@login_required
@csrf
def edit(id):
    status = Status()
    username = open_session()['u']
    title_form = EventTitle(request.forms)
    datetime_form = EventDateTime(request.forms)
    location_form = EventLocation(request.forms)
    description_form = EventDescription(request.forms)
    flags_form = EventFlags(request.forms)
    if request.method == 'POST' and\
       request.query['field'] == 'title':
        if title_form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(events.update().values(
                    title=title_form.title.data).where(
                        and_(
                            events.c.user_id == username,
                            events.c.id == id)))
                conn.close()
            except exc.SQLAlchemyError as message:
                    status.danger = message
            else:
                status.success = "Updated title"
    if request.method == 'POST' and\
       request.query['field'] == 'datetime':
        if datetime_form.validate():
            try:
                event_datetime = datetime.strptime(
                    datetime_form.date.data + ' ' + datetime_form.time.data,
                    '%Y/%m/%d %I:%M %p')
            except:
                status.danger = "Date or time not in valid format. " +\
                                "Use selector buttons to select date and time"
            else:
                try:
                    conn = db.engine.connect()
                    conn.execute(events.update().values(
                                 event_datetime=event_datetime).where(
                                     and_(
                                         events.c.user_id == username,
                                         events.c.id == id)))
                    conn.close()
                except exc.SQLAlchemyError as message:
                    status.danger = message
                else:
                    status.success = "Updated date/time"
    if request.method == 'POST' and\
       request.query['field'] == 'location':
        if location_form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(events.update().values(
                    location=location_form.location.data).where(
                        and_(
                            events.c.user_id == username,
                            events.c.id == id)))
                conn.close()
            except exc.SQLAlchemyError as message:
                    status.danger = message
            else:
                status.success = "Updated location"
    if request.method == 'POST' and\
       request.query['field'] == 'description':
        if description_form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(description_update,
                             description=description_form.description.data,
                             username=username,
                             id=id)
                conn.close()
            except exc.SQLAlchemyError as message:
                status.danger = message
            else:
                status.success = "Updated description"
    if request.method == 'POST' and\
       request.query['field'] == 'flags':
        if flags_form.validate():
            try:
                conn = db.engine.connect()
                conn.execute(flags_update,
                             datetime=flags_form.datetime.data,
                             location=flags_form.location.data,
                             canceled=flags_form.canceled.data,
                             username=username,
                             id=id)
                conn.close()
            except exc.SQLAlchemyError as message:
                status.danger = message
            else:
                status.success = "Updated flags"
    conn = db.engine.connect()
    result = conn.execute(select,
                          id=id, username=username)
    conn.close()
    row = result.fetchone()
    title_form.title.data = row['title']
    description_form.description.data = row['description']
    flags_form.datetime.data = bool(row['datetime_changed'])
    flags_form.location.data = bool(row['location_changed'])
    flags_form.canceled.data = bool(row['canceled'])
    current_datetime = row['event_datetime']
    current_location = row['location']
    return dict(status=status,
                event_id=row['id'],
                current_datetime=current_datetime,
                current_location=current_location,
                title_form=title_form,
                datetime_form=datetime_form,
                location_form=location_form,
                description_form=description_form,
                flags_form=flags_form)
